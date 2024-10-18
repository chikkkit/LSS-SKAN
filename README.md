# LSS-SKAN
<p align="center"><b>English</b> / <a href="https://github.com/chikkkit/LSS-SKAN/blob/main/README_zh.md">简体中文</a></p>

## Statement
This is the experimental code for the paper "LSS-SKAN: Efficient Kolmogorov–Arnold Networks based on Single-Parameterized Function" [1]. It includes:  
- the preliminary experiment (preExp.py), 
- Experiment 1 - Comparison of various SKANs under 10-epoch training (MLP_SSPKAN_10epoch_skans.py),   
- Experiment 2 - Comparison of LSS-SKAN with other popular KAN variants under 10-epoch training (MLP_SSPKAN_10epoch.py),   
- Experiment 3 - Comparison of LSS-SKAN with other popular KAN variants under 30-epoch training (MLP_SSPKAN_30epoch_lr000101.py).  

**If you're looking for a Python library to quickly build SKAN, click [here](https://github.com/chikkkit/SKAN) to visit the GitHub repository of the skan library.**

This library references code from [WavKAN](https://github.com/zavareh1/Wav-KAN)[2], [EfficientKAN](https://github.com/Blealtan/efficient-kan)[3], [FastKAN](https://github.com/ZiyaoLi/fast-kan)[4], and [FourierKAN](https://github.com/GistNoesis/FourierKAN)[5]. These codes are placed in the modelnetwork folder and are mainly used for model comparison. The paper also compares [fKAN](https://github.com/alirezaafzalaghaei/fKAN)[6] and [rKAN](https://github.com/alirezaafzalaghaei/rKAN)[7], which are called as Python libraries.

## Usage
This code runs under Python 3.12.3. To use the library code, make sure you have the following Python libraries installed:
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
Then execute the scripts to run the code:
```bash
python preExp.py
python MLP_SSPKAN_10epoch_skans.py
python MLP_SSPKAN_10epoch.py
python MLP_SSPKAN_30epoch_lr000101.py
```
This will run the four experiments from the paper.

## File Description
```
LSS_SKAN_Experiment_Code
├─ MLP_SSPKAN_10epoch.py  # Experiment 2 - Comparison of LSS-SKAN with other popular KAN variants under 10-epoch training
├─ MLP_SSPKAN_10epoch_skans.py  # Experiment 1 - Comparison of various SKANs under 10-epoch training
├─ MLP_SSPKAN_30epoch_lr000101.py  # Experiment 3 - Comparison of LSS-SKAN with other popular KAN variants under 30-epoch training
├─ preExp.py  # Preliminary experiment code
└─ modelnetwork  # Network implementation code folder
   ├─ efficientKAN.py
   ├─ fastkan.py
   ├─ fftKAN.py
   ├─ skan_exp_version.py  # SKAN network implementation code
   └─ wavKAN.py
```

## Reference
[1] LSS-SKAN: Efficient Kolmogorov–Arnold Networks based on Single-Parameterized Function(submited to arxiv)  
[2] WavKAN, https://github.com/zavareh1/Wav-KAN  
[3] EfficientKAN, https://github.com/Blealtan/efficient-kan  
[4] FastKAN, https://github.com/ZiyaoLi/fast-kan  
[5] FourierKAN, https://github.com/GistNoesis/FourierKAN  
[6] fkan, https://github.com/alirezaafzalaghaei/fKAN  
[7] rkan, https://github.com/alirezaafzalaghaei/rKAN  
