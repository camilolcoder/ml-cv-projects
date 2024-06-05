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
fbRange = [6200, 6800]
pError = 0
startCounter = 1


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
    faces = faceCascade.detectMultiScale(imgGray, 1.2, 8)

    myFacesListC = []
    myFaceListArea = []

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cx = x + w//2
        cy = y + h//2
        area = w*h
        cv2.circle(img, (cx, cy), 5, (0, 255, 0), cv2.FILLED)
        myFacesListC.append([cx,cy])
        myFaceListArea.append(area)

    if len(myFaceListArea) != 0:
        i = myFaceListArea.index(max(myFaceListArea))
        # index of closest face
        return img,[myFacesListC[i],myFaceListArea[i]]
    else:
        return img, [[0,0],0]

def findUpperBody(img):
    faceCascade = cv2.CascadeClassifier("haarcascade_upperbody.xml")
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, 1.2, 8)

    myFacesListC = []
    myFaceListArea = []

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cx = x + w//2
        cy = y + h//2
        area = w*h
        cv2.circle(img, (cx, cy), 5, (0, 255, 0), cv2.FILLED)
        myFacesListC.append([cx,cy])
        myFaceListArea.append(area)

    if len(myFaceListArea) != 0:
        i = myFaceListArea.index(max(myFaceListArea))
        # index of closest face
        return img,[myFacesListC[i],myFaceListArea[i]]
    else:
        return img, [[0,0],0]

def trackFace(myDrone,info,w,pid,pError):
    area = info[1]
    x, y = info[0]
    fb = 0
    
    error = c[0][0] - w//2   
    speed = pid[0] * error + pid[1] * (error - pError)
    speed = int(np.clip(speed, -100, 100))
#<
    if area > fbRange[0] and area < fbRange[1]:
        fb = 0
    elif area > fbRange[1]:
        fb = -20
    elif area < fbRange[0] and area != 0:
        fb = 20
    
    print(speed, fb)

    if x == 0:
        speed = 0
        error = 0
    
    myDrone.send_rc_control(0, fb, 0, speed)

    return error


#myDrone = intializeTello()

car = 1
#time.sleep(4)
cap = cv2.VideoCapture(0) # To be able to use external logitech camera I have to turn it on using the logitech app

while True:

    _, img = cap.read()
    #img = telloGetFrame(myDrone)
    img, c = findFace(img)
    #img, c = findUpperBody(img)
    #pError = trackFace(myDrone,c,w,pid,pError)

    # if car == 0:
    #     myDrone.takeoff()
    #     myDrone.send_rc_control(0, 0, 40, 0)
    #     car = 1

    cv2.imshow("Follow", img)
    cv2.waitKey(1)
    # if cv2.waitKey(1) and 0xFF == ord('q'):
    # # replace the 'and' with '&amp;'
    #     myDrone.land()
    #     break
    