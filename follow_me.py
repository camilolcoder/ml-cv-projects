#from pyimagesearch.objcenter import ObjCenter
import cv2
from simple_pid import PID
from djitellopy import Tello
import signal
import sys
#import imutils
import time
from datetime import datetime
from multiprocessing import Manager, Process, Pipe, Event
import numpy as np

w, h = 360, 240
pid = [0.5, 0.5, 0]
pError = 0
startCounter = 0


def intializeTello():
# CONNECT TO TELLO
    myDrone = Tello()
    myDrone.connect()
    myDrone.for_back_velocity = 0
    myDrone.left_right_velocity = 0
    myDrone.up_down_velocity = 0
    myDrone.yaw_velocity = 0
    myDrone.speed =0
    print(myDrone.get_battery())
    myDrone.streamoff()
    myDrone.streamon()
    return myDrone

def telloGetFrame(myDrone,w=360,h=240):
    # GET THE IMGAE FROM TELLO
    myFrame = myDrone.get_frame_read()
    myFrame = myFrame.frame
    img = cv2.resize(myFrame, (w, h))
    return img

def findFace(img):
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)

    myFacesListC = []
    myFaceListArea = []

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cx = x + w//2
        cy = y + h//2
        area = w*h
        myFacesListC.append([cx,cy])
        myFaceListArea.append(area)

    if len(myFaceListArea) != 0:
        i = myFaceListArea.index(max(myFaceListArea))
        # index of closest face
        return img,[myFacesListC[i],myFaceListArea[i]]
    else:
        return img, [[0,0],0]

def trackFace(myDrone,c,w,pid,pError):
    print(c)
    error = c[0][0] - w//2   
    # Current Value - Target Value
    if pError is not None:
        speed = int(pid[0] * error + pid[1] * (error - pError))
    else:
        speed = int(pid[0] * error)
    speed = np.clip(speed, -100, 100)
    print(speed)

    if c[0][0] != 0:
        myDrone.yaw_velocity = speed
    else:
        myDrone.left_right_velocity = 0
        myDrone.for_back_velocity = 0
        myDrone.up_down_velocity = 0
        myDrone.yaw_velocity = 0
        error = 0
    # SEND VELOCITY VALUES TO TELLO
    if myDrone.send_rc_control:
        myDrone.send_rc_control(myDrone.left_right_velocity,myDrone.for_back_velocity,
        myDrone.up_down_velocity, myDrone.yaw_velocity)

    return error


myDrone = intializeTello()

while True:

    if startCounter == 0:
        myDrone.takeoff()
        startCounter = 1

    ## STEP 1
    img = telloGetFrame(myDrone)
    # WAIT FOR THE 'Q' BUTTON TO STOP
    ## STEP 2
    img, c = findFace(img)
    ## STEP 3
    if len(c) != 0:
        pError = trackFace(myDrone,c,w,pid,pError)
    else:
        pError = 0

    cv2.imshow("Follow", img)
    if cv2.waitKey(1) and 0xFF == ord('q'):
    # replace the 'and' with '&amp;'
        myDrone.land()
        break
    