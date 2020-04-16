'''
Created on Apr 16, 2020


@author: myuey
'''
import ffmpy 
import csv
import cv2
from collections import defaultdict
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import os

#converts between different video formats 
def convertFormat(inputFile, outputFile):
    ff = ffmpy.FFmpeg(
        inputs={inputFile : None},
        outputs={outputFile: None}
    )
    ff.run()
#creates directory of tagged videos from an input csv file and an input video file 
#rows start at 1
#get the sign label from column 2
#end frames from column 9
#start frames from column 8
def tagger(inputFile, inputVid, outputDir, frameBufferValue, startRow, startCol, endCol, labelCol):
    columns = defaultdict(list)
    #amount of frames on either side
    #open csv file
    rowCounter = 0
    with open(inputFile, newline = '') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            for (i,v) in enumerate(row):
                columns[i].append(v)
            #get the sign label from column 2
            if(rowCounter > startRow):
                #get sign label
                signLabel = columns[labelCol][rowCounter]   
                #get the frames that the label is associated with             
                startFrame = int(columns[startCol][rowCounter]) - frameBufferValue              
                endFrame = int(columns[endCol][rowCounter]) + frameBufferValue
                #get frame rate of video
                cap = cv2.VideoCapture(inputVid)
                fps = cap.get(cv2.CAP_PROP_FPS)
                #get timestamps using fps and frame numbers
                startTime = startFrame/fps
                endTime = endFrame/fps
                # create directory if it doesnt exist
                if not os.path.exists(outputDir):
                    os.makedirs(outputDir)
                #create a new video file containing only the frames indicated
                ffmpeg_extract_subclip(inputVid, startTime ,endTime, targetname= outputDir+ signLabel + ".avi")
                print(str(rowCounter) + " " + signLabel + " " + str(startTime) + " " + str(endTime))
            rowCounter += 1
    
        