'''
Created on Apr 29, 2020

@author: myuey
'''

from util import vidUtil
inputDir1 = "./videoConvert/videoInLanaConverted/"
csvInput1 = "./csvdata/input1-Lana1.csv"
outputDir1 = "./taggedVideo/lanaTagged"

vidUtil.tagger(csvInput1, inputDir1, outputDir1, 1, 0)

inputDir2 = "./videoConvert/videoInDanaConverted/"
csvInput2 = "./csvdata/input2-Dana1.csv"
outputDir2 = "./taggedVideo/danaTagged"

vidUtil.tagger(csvInput2, inputDir2, outputDir2, 1, 0)

inputDir3 = "./videoConvert/videoInLiz01-11Converted/"
csvInput3 = "./csvdata/input3-Liz1.csv"
outputDir3 = "./taggedVideo/lizTagged/"

vidUtil.tagger(csvInput3, inputDir3, outputDir3, 1, 490)
vidUtil.tagger(csvInput3, inputDir3, outputDir3, 1548, 1563)

inputDir4 = "./videoConvert/videoInLiz01-18Converted/"

vidUtil.tagger(csvInput3, inputDir4, outputDir3, 489, 982)
vidUtil.tagger(csvInput3, inputDir4, outputDir3, 1562, 1565)

inputDir5 = "./videoConvert/videoInLiz02-01Converted/"

vidUtil.tagger(csvInput3, inputDir5, outputDir3, 981, 1472)
vidUtil.tagger(csvInput3, inputDir5, outputDir3, 1563, 1577)

inputDir6 = "./videoConvert/videoInLiz02-15Converted/"

vidUtil.tagger(csvInput3, inputDir6, outputDir3, 1471, 1549)

inputDir7 = "./videoConvert/videoInTyler05-12aConverted/"
csvInput4 = "./csvdata/input4-Tyler1.csv"
outputDir4 = "./taggedVideo/tylerTagged/"

vidUtil.tagger(csvInput4, inputDir7, outputDir4, 1, 431)
vidUtil.tagger(csvInput4, inputDir7, outputDir4, 1373, 1388)

inputDir8 = "./videoConvert/videoInTyler05-12bConverted/"
vidUtil.tagger(csvInput4, inputDir8, outputDir4, 430, 595)
vidUtil.tagger(csvInput4, inputDir8, outputDir4, 1387, 1397)

inputDir9 = "./videoConvert/videoInTyler05-29aConverted/"
vidUtil.tagger(csvInput4, inputDir9, outputDir4, 594, 1018)
vidUtil.tagger(csvInput4, inputDir9, outputDir4, 1396, 1429)

inputDir10 = "./videoConvert/videoInTyler05-29bConverted/"
vidUtil.tagger(csvInput4, inputDir10, outputDir4, 1017, 1184)
vidUtil.tagger(csvInput4, inputDir10, outputDir4, 1428, 1433)

inputDir11 = "./videoConvert/videoInTyler06-10Converted/"
vidUtil.tagger(csvInput4, inputDir11, outputDir4, 1183, 1374)

inputDir12 = "./videoConvert/videoInNaomi08-04Converted/"
csvInput5 = "./csvdata/input5-Naomi1.csv"
outputDir5 = "./taggedVideo/naomiTagged/"
vidUtil.tagger(csvInput5, inputDir12, outputDir5, 1, 454)
vidUtil.tagger(csvInput5, inputDir12, outputDir5, 1383, 1389)

inputDir13 = "./videoConvert/videoInNaomi08-06Converted/"
vidUtil.tagger(csvInput5, inputDir13, outputDir5, 453, 927)

inputDir14 = "./videoConvert/videoInNaomi08-13Converted/"
vidUtil.tagger(csvInput5, inputDir14, outputDir5, 926, 1262)

inputDir15 = "./videoConvert/videoInNaomi08-13bConverted/"
vidUtil.tagger(csvInput5, inputDir15, outputDir5, 1261, 1384)

inputDir16 = "./videoConvert/videoInJaimee10-10Converted/"
csvInput6 = "./csvdata/input6-Jaimee1.csv"
outputDir6 = "./taggedVideo/jaimeeTagged/"
vidUtil.tagger(csvInput6, inputDir16, outputDir6, 1, 0)