# LSS-SKAN

## 声明
这是论文LSS-SKAN: Efficient Kolmogorov–Arnold Networks based on Single-Parameterized Function[1]中的实验代码，包含:
- 预实验(preExp.py)，
- 实验1——10epoch训练下各SKAN对比(MLP_SSPKAN_10epoch_skans.py)
- 实验2——10epoch训练下LSS-SKAN与其他热门KAN变体的对比(MLP_SSPKAN_10epoch.py)
- 实验3——30epoch训练下LSS-SKAN与其他热门KAN变体的对比(MLP_SSPKAN_30epoch_lr000101.py)。

**如果你正在寻找用于快速构建SKAN的Python库，点击[这里](https://github.com/chikkkit/SKAN)前往skan库的github仓库。**

该库引用了[WavKAN](https://github.com/zavareh1/Wav-KAN)[2]，[EfficientKAN](https://github.com/Blealtan/efficient-kan)[3]，[FastKAN](https://github.com/ZiyaoLi/fast-kan)[4]和[FourierKAN](https://github.com/GistNoesis/FourierKAN)[5]库的代码，这些代码放置在modelnetwork文件夹里，主要用于模型对比。文章还对比了[fKAN](https://github.com/alirezaafzalaghaei/fKAN)[6]和[rKAN](https://github.com/alirezaafzalaghaei/rKAN)[7], 这些算法以Python库的形式被调用。

## 使用
本代码是在Python3.12.3下运行的。要使用该库代码，请确保安装了如下Python库：
```
fkan==0.0.2
numpy==2.1.2
pandas==2.2.3
rkan==0.0.3
scikit-learn==1.5.2
torch==2.4.1+cu121
torchvision==0.19.1+cu121
tqdm==4.66.4
```
然后执行脚本运行代码：
```bash
python preExp.py
python MLP_SSPKAN_10epoch_skans.py
python MLP_SSPKAN_10epoch.py
python MLP_SSPKAN_30epoch_lr000101.py
```
这将运行文章的四个实验。

## 文件说明
```
LSS_SKAN_Experiment_Code
├─ MLP_SSPKAN_10epoch.py  # 实验2——10epoch训练下LSS-SKAN与其他热门KAN变体的对比
├─ MLP_SSPKAN_10epoch_skans.py  # 实验1——10epoch训练下各SKAN对比
├─ MLP_SSPKAN_30epoch_lr000101.py  # 实验3——30epoch训练下LSS-SKAN与其他热门KAN变体的对比
├─ preExp.py  # 预实验代码
└─ modelnetwork  # 网络实现代码文件夹
   ├─ efficientKAN.py
   ├─ fastkan.py
   ├─ fftKAN.py
   ├─ skan_exp_version.py  # SKAN网络实现代码
   └─ wavKAN.py
```[

## 引用
[1] LSS-SKAN: Efficient Kolmogorov–Arnold Networks based on Single-Parameterized Function(submited to arxiv)
[2] WavKAN, https://github.com/zavareh1/Wav-KAN
[3] EfficientKAN, https://github.com/Blealtan/efficient-kan
[4] FastKAN, https://github.com/ZiyaoLi/fast-kan
[5] FourierKAN, https://github.com/GistNoesis/FourierKAN
[6] fkan, https://github.com/alirezaafzalaghaei/fKAN
[7] rkan, https://github.com/alirezaafzalaghaei/rKAN
