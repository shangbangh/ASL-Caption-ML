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
#converts all videos in input directory to avi video format in output directory    
def convertAll(inputDir, outputDir):
    inputVids = os.listdir(inputDir)
    if not os.path.exists(outputDir):
        os.makedirs(outputDir)
    outputDir = outputDir + "/"
    inputDir = inputDir + "/"
    for vid in inputVids:
        vidStr = "".join(vid[0:len(vid) - 4:1]) + ".avi"
        print(vidStr)       
        convertFormat(inputDir + vid, outputDir + vidStr)
    
#returns {width, height} of input video as integers   
def getResolution(inputVid):
    vid = cv2.VideoCapture(inputVid)
    width = vid.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
    return {width, height}

#gets the fps of the input video
def getFPS(inputVid):
    vid = cv2.VideoCapture(inputVid)
    fps = vid.get(cv2.CAP_PROP_FPS) 
    return fps    

#creates directory of tagged videos from an input csv file and an input video file directory
#rows start at 1 
#get the sign label from column 2
#end frames from column 9
#start frames from column 8
#video number from column 5
#if endrow is 0 or less than startrow, reads entire file
def tagger(inputFile, inputVidDir, outputDir, startRow, endRow):
    #amount of frames on either side
    frameBufferValue = 20
    startCol = 8
    endCol = 9
    labelCol = 2
    vidCol = 5
    
    columns = defaultdict(list)
    #open csv file
    rowCounter = 0
    with open(inputFile, newline = '') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            for (i,v) in enumerate(row):
                columns[i].append(v)
            #get the video number in the row
            vidNum = columns[vidCol][rowCounter]
            #get the video number from the input video
            vidString = "scene{num}-camera1.avi".format(num = vidNum)
            
            inputVid = inputVidDir + vidString
            #get the sign label from column 2
            
            if(endRow < startRow):
                if(rowCounter > startRow):
                    #get sign label
                    signLabel = columns[labelCol][rowCounter]   
                    print(vidString + " " + signLabel)
                    #get the frames that the label is associated with             
                    startFrame = int(columns[startCol][rowCounter]) - frameBufferValue              
                    endFrame = int(columns[endCol][rowCounter]) + frameBufferValue
                    #get frame rate of video
                    fps = getFPS(inputVid)
                    if(fps == 0):
                        break
                    #get timestamps using fps and frame numbers
                    startTime = startFrame/fps
                    endTime = endFrame/fps
                    # create directory if it doesnt exist
                    if not os.path.exists(outputDir):
                        os.makedirs(outputDir)
                    #create a new video file containing only the frames indicated
                    ffmpeg_extract_subclip(inputVid, startTime ,endTime, targetname= outputDir + '/'+ signLabel + ".avi")
                rowCounter += 1
            else:
                if(rowCounter > startRow and rowCounter < endRow):
                    #get sign label
                    signLabel = columns[labelCol][rowCounter]   
                    print(vidString + " " + signLabel)
                    #get the frames that the label is associated with             
                    startFrame = int(columns[startCol][rowCounter]) - frameBufferValue              
                    endFrame = int(columns[endCol][rowCounter]) + frameBufferValue
                    #get frame rate of video
                    fps = getFPS(inputVid)
                    if(fps == 0):
                        break
                    #get timestamps using fps and frame numbers
                    startTime = startFrame/fps
                    endTime = endFrame/fps
                    # create directory if it doesnt exist
                    if not os.path.exists(outputDir):
                        os.makedirs(outputDir)
                    #create a new video file containing only the frames indicated
                    ffmpeg_extract_subclip(inputVid, startTime ,endTime, targetname= outputDir + '/'+ signLabel + ".avi")
                rowCounter += 1
