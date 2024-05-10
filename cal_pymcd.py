from pymcd.mcd import Calculate_MCD
import os
import json
import argparse
import numpy as np
from tqdm import tqdm
import pprint


#gt_wav='results/outputs/mask_cyclegan_vc_VCC2SM3_VCC2SF3/converted_audio/0-original_VCC2SM3_to_VCC2SF3.wav' 
#converted_wav='results/outputs/mask_cyclegan_vc_VCC2SM3_VCC2SF3/converted_audio/0-converted_VCC2SM3_to_VCC2SF3.wav'


gt_wav='' 
converted_wav=''

def calculate_mcd(gt_wav, converted_wav, mcd_mode='dtw'):
    mcd_toolbox = Calculate_MCD(MCD_mode=mcd_mode)
    mcd_result = mcd_toolbox.calculate_mcd(gt_wav, converted_wav)
    print(mcd_result)

calculate_mcd(gt_wav, converted_wav)