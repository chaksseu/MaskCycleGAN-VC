# MaskCycleGAN-VC Experiment

본 레포지토리는 아래 링크의 original code를 쉽게 실험할 수 있도록 수정한 버전입니다.

코드에 대해 자세히 이해하고 싶으시다면 paper와 original repo link를 참고해주세요.

Paper: https://arxiv.org/pdf/2102.12841.pdf

Original repo link(non-official): https://github.com/GANtastic3/MaskCycleGAN-VC


## 코드 베이스 다운 및 아나콘다 환경 설정

Clone the repository

```
git clone https://github.com/chaksseu/MaskCycleGAN-VC.git
cd MaskCycleGAN-VC
```

아나콘다 환경 설정 및 필요 패키지 설치

```
conda create -n MaskCycleGAN-VC python==3.9.2
conda activate MaskCycleGAN-VC
pip install -r requirements.txt
```


## 데이터셋 준비

아래 command line을 통해 VCC2018데이터셋을 다운받을 수 있습니다. 

```
wget --no-check-certificate https://datashare.ed.ac.uk/bitstream/handle/10283/3061/vcc2018_database_training.zip?sequence=2&isAllowed=y
wget --no-check-certificate https://datashare.ed.ac.uk/bitstream/handle/10283/3061/vcc2018_database_evaluation.zip?sequence=3&isAllowed=y
wget --no-check-certificate https://datashare.ed.ac.uk/bitstream/handle/10283/3061/vcc2018_database_reference.zip?sequence=5&isAllowed=y
```

압축 해제 및 데이터셋 폴더 정리

```
mkdir vcc2018
apt-get install unzip
unzip vcc2018_database_training.zip?sequence=2 -d vcc2018/
unzip vcc2018_database_evaluation.zip?sequence=3 -d vcc2018/
unzip vcc2018_database_reference.zip?sequence=5 -d vcc2018/
mv -v vcc2018/vcc2018_reference/* vcc2018/vcc2018_evaluation
rm -rf vcc2018/vcc2018_reference
```

추가로 개별적인 데이터셋을 학습에 이용하시려면, 생성된 vcc2018_evaluation과 vcc2018_training 폴더 아래에 원하시는 화자 이름을 폴더를 생성하신 후, 그 안에 해당 화자의 wav파일를 넣어주시면 됩니다.

vcc2018_training -> 모델 훈련에 사용되는 데이터셋

vcc2018_evaluation -> 모델 테스트에 사용되는 데이터셋

## 데이터 전처리

```
python data_preprocessing/preprocess_vcc2018.py \
  --data_directory vcc2018/vcc2018_training \
  --preprocessed_data_directory vcc2018_preprocessed/vcc2018_training \
  --speaker_ids VCC2SF1 VCC2SF2 VCC2SF3 VCC2SF4 VCC2SM1 VCC2SM2 VCC2SM3 VCC2SM4 VCC2TF1 VCC2TF2 VCC2TM1 VCC2TM2
```

```
python data_preprocessing/preprocess_vcc2018.py \
  --data_directory vcc2018/vcc2018_evaluation \
  --preprocessed_data_directory vcc2018_preprocessed/vcc2018_evaluation \
  --speaker_ids VCC2SF1 VCC2SF2 VCC2SF3 VCC2SF4 VCC2SM1 VCC2SM2 VCC2SM3 VCC2SM4 VCC2TF1 VCC2TF2 VCC2TM1 VCC2TM2
```

`--speaker_ids` 뒤에 적은 화자들의 데이터셋이 전처리됩니다.


## 모델 학습

`<speaker_A_id>`를 source로 `<speaker_B_id>`를 target으로 하는 모델을 훈련합니다. 최소 수백 epoch 이상으로 훈련시키는 것을 권장합니다.

```
python -W ignore::UserWarning -m mask_cyclegan_vc.train \
    --name mask_cyclegan_vc_<speaker_id_A>_<speaker_id_B> \
    --seed 0 \
    --save_dir results/ \
    --preprocessed_data_dir vcc2018_preprocessed/vcc2018_training/ \
    --speaker_A_id <speaker_A_id> \
    --speaker_B_id <speaker_B_id> \
    --epochs_per_save 10 \
    --epochs_per_plot 10 \
    --num_epochs 6172 \
    --batch_size 1 \
    --lr 5e-4 \
    --decay_after 1e4 \
    --sample_rate 22050 \
    --num_frames 64 \
    --max_mask_len 25 \
    --gpu_ids 0 \
```

이전 학습에 이어서 학습하시려면 위 코드 뒤에 `--continue_train`을 추가하시면 자동적으로 최신 epoch에 이어서 학습이 진행됩니다.


## 모델 테스트 (오디오 생성)

훈련시킨 MaskCycleGAN-VC 모델을 evaluation dataset으로 test합니다. 

converted audio는 다음 위치에 저장됩니다. `results/<name>/converted_audio`.

```
python -W ignore::UserWarning -m mask_cyclegan_vc.test \
    --name mask_cyclegan_vc_<speaker_A_id>_<speaker_B_id> \
    --save_dir results/ \
    --preprocessed_data_dir vcc2018_preprocessed/vcc2018_evaluation \
    --gpu_ids 0 \
    --speaker_A_id <speaker_A_id> \
    --speaker_B_id <speaker_B_id> \
    --ckpt_dir /data1/cycleGAN_VC3/mask_cyclegan_vc_<speaker_A_id>_<speaker_B_id>/ckpts \
    --load_epoch <the epoch you want> \
    --model_name generator_A2B \
```

## 코드 구조
```
├── README.md                       <- Top-level README.
├── environment.yml                 <- Conda environment
├── requirements.txt                <- required python packages
├── .gitignore
├── LICENSE
|
├── args
│   ├── base_arg_parser             <- arg parser
│   ├── train_arg_parser            <- arg parser for training (inherits base_arg_parser)
│   ├── cycleGAN_train_arg_parser   <- arg parser for training MaskCycleGAN-VC (inherits train_arg_parser)
│   ├── cycleGAN_test_arg_parser    <- arg parser for testing MaskCycleGAN-VC (inherits base_arg_parser)
│
├── bash_scripts
│   ├── mask_cyclegan_train.sh      <- sample script to train MaskCycleGAN-VC
│   ├── mask_cyclegan_test.sh       <- sample script to test MaskCycleGAN-VC
│
├── data_preprocessing
│   ├── preprocess_vcc2018.py       <- preprocess VCC2018 dataset
│
├── dataset
│   ├── vc_dataset.py               <- torch dataset class for MaskCycleGAN-VC
│
├── logger
│   ├── base_logger.sh              <- logging to Tensorboard
│   ├── train_logger.sh             <- logging to Tensorboard during training (inherits base_logger)
│
├── saver
│   ├── model_saver.py              <- saves and loads models
│
├── mask_cyclegan_vc
│   ├── model.py                    <- defines MaskCycleGAN-VC model architecture
│   ├── train.py                    <- training script for MaskCycleGAN-VC
│   ├── test.py                     <- training script for MaskCycleGAN-VC
│   ├── utils.py                    <- utility functions to train and test MaskCycleGAN-VC

```