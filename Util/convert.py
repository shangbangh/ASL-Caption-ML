'''
Created on Apr 29, 2020

@author: myuey
'''
import os 
from util import vidUtil

inputBigDir = "./videoIn/"
outputDir = "./videoConvert/"

listDir = os.listdir(inputBigDir)

for inputDir in listDir:
    convertDir = inputDir + "Converted/"
    vidUtil.convertAll(inputBigDir + inputDir + "/",outputDir + convertDir)
