from pymcd.mcd import Calculate_MCD
import os
import json
import argparse
import numpy as np
from tqdm import tqdm
import pprint


#gt_wav='results/mask_cyclegan_vc_VCC2SF2_VCC2SM2/converted_audio/0-original_VCC2SF2_to_VCC2SM2.wav' 
#converted_wav='results/mask_cyclegan_vc_VCC2SF2_VCC2SM2/converted_audio/0-converted_VCC2SF2_to_VCC2SM2.wav'


gt_wav='' 
converted_wav=''

def calculate_mcd(gt_wav, converted_wav, mcd_mode='dtw'):
    mcd_toolbox = Calculate_MCD(MCD_mode=mcd_mode)
    mcd_result = mcd_toolbox.calculate_mcd(gt_wav, converted_wav)
    print(mcd_result)

calculate_mcd(gt_wav, converted_wav)