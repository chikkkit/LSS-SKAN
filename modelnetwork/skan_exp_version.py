import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.utils.data import DataLoader
from torch.utils.data import Dataset
import numpy as np
import torch

## 定义一些单参数非线性函数
# y = max(0, x), ReLU
def lrelu(x, k):
    return torch.clamp(k*x, min=0)

# y = max(kx, x), leaky ReLU
def lleaky_relu(x, k):
    return torch.max(k*x, x)

# y = x / (1 + e^(-kx)), Swish
def lswish(x, k):
    return x / (1 + torch.exp(-k*x))

# y = x / (1 + e^(-kx)), Mish
def lmish(x, k):
    return x * torch.tanh(torch.log(1 + torch.exp(k*x)))

# y = log(1 + e^(kx)), Softplus
def lsoftplus(x, k):
    return torch.log(1 + torch.exp(k*x))

# y = max(0, min(1, (kx + 0.5))), Hard sigmoid
def lhard_sigmoid(x, k):
    return torch.clamp(k*x + 0.5, min=0, max=1)

# y = k * (e^(x/k) - 1) if x < 0, else x, Exponential Linear Unit (ELU)
def lelu(x, k):
    return torch.where(x < 0, k * (torch.exp(x/k) - 1), x)

# y = log(1 + e^(kx)) - log(2), Shifted Softplus
def lshifted_softplus(x, k):
    return torch.log(1 + torch.exp(k*x)) - np.log(2)

# y = 0.5 * x * (1 + tanh(sqrt(2/pi) * (kx + 0.044715 * k^3 * x^3))), Gaussian Error Linear Unit with Parameter (GELU-P)
def lgelup(x, k):
    return 0.5 * x * (1 + torch.tanh(np.sqrt(2/np.pi) * (k*x + 0.044715 * k**3 * x**3)))

class SKANLinear(nn.Module):
    def __init__(self, in_features, out_features, bias=True, base_function=lrelu, device='cpu'):
        super(SKANLinear, self).__init__()
        self.in_features = in_features
        self.out_features = out_features
        self.use_bias = bias
        self.base_function = base_function
        self.device = device
        if bias:
            self.weight = nn.Parameter(torch.Tensor(out_features, in_features+1).to(device))
        else:
            self.weight = nn.Parameter(torch.Tensor(out_features, in_features).to(device))
        self.reset_parameters()

    def reset_parameters(self):
        nn.init.kaiming_uniform_(self.weight, a=5**0.5)
    
    def forward(self, x):
        x = x.view(-1, 1, self.in_features)
        # 添加偏置单元
        if self.use_bias:
            x = torch.cat([x, torch.ones_like(x[..., :1])], dim=2)

        y = self.base_function(x, self.weight)
        
        y = torch.sum(y, dim=2)
        return y
    
    def extra_repr(self):
        return 'in_features={}, out_features={}'.format(
            self.in_features, self.out_features
        )
    
class SKANNetwork(nn.Module):
    def __init__(self, layer_sizes, base_function=lrelu, bias=True, device='cpu'):
        super(SKANNetwork, self).__init__()
        self.layers = nn.ModuleList()
        for i in range(len(layer_sizes)-1):
            self.layers.append(SKANLinear(layer_sizes[i], layer_sizes[i+1], bias=bias, 
                                             base_function=base_function, device=device))
    
    def forward(self, x):
        for layer in self.layers:
            x = layer(x)
        return x
    
__all__ = [
    'lrelu', 'lleaky_relu', 'lswish', 'lmish', 'lsoftplus', 
    'lhard_sigmoid', 'lelu', 'lshifted_softplus', 'lgelup',
    'SKANLinear', 'SKANNetwork'
]