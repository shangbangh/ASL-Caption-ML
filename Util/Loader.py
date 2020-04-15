import numpy as np
import cv2 as cv
'''
Created on Apr 15, 2020

@author: Shangbang
'''

    
def LoadVideo(vidPath):
    cap = cv.VideoCapture(vidPath)
    while cap.isOpened():
        ret, frame = cap.read()
        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        cv.imshow('frame', gray)
        if cv.waitKey(1) == ord('q'):
            break
    cap.release()
    cv.destroyAllWindows()