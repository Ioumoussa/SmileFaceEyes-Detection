# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 16:00:35 2019

@author: hp
"""
import cv2
import time

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')

#definiig a function that will do the detection
def detect(gray , frame):
    faces = face_cascade.detectMultiScale(gray, 1.3 , 5)
    # detect the rectangle that will detect the face
 #faces is table of for elements which are x,y, the width , and the hight
    for(x,y,h,w) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 147, 0), 2 )
        roi_gray  = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 3)  
        for(ex,ey,eh,ew) in eyes:
            cv2.rectangle(roi_color, (ex,ey), (ex+ew,ey+eh), (113,255,122), 2)
        smiles = smile_cascade.detectMultiScale(roi_gray, 1.7, 22)
        for (sx, sy, sw, sh) in smiles:
            cv2.rectangle(roi_color, (sx, sy), (sx+sw, sy+sh), (0, 0, 255), 2)     
    
    return frame
            
#applyintg the detect function with my web cam

video_capture = cv2.VideoCapture(0)
while True:
    ret , frame = video_capture.read()
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
    can = detect(gray , frame)   
    
    cv2.imshow('blablla',can)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()   



























