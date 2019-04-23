"""Access IP Camera in Python OpenCV"""

import cv2
import face_recognition
from PIL import Image, ImageFont, ImageDraw, ImageEnhance
import os,numpy
import datetime


stream = cv2.VideoCapture('rtsp://admin:12345@192.168.2.180/1')  


while True:
    r, f = stream.read()
    small_frame = cv2.resize(f, (0, 0), fx=0.25, fy=0.25)
    mil = small_frame[:, :, ::-1]
    face_locations = face_recognition.face_locations(mil)
    if len(face_locations)==0:
        print("NO ONE !")

    for x1,y1,x2,y2 in face_locations:
        a1 = max(x1,x2)*4
        b1 = max(y1,y2)*4
        a2 = min(x1,x2)*4
        b2 = min(y1,y2)*4  
        cv2.rectangle(f, (b2, a2),( b1, a1), (0, 255, 0), 5)
        font = cv2.FONT_HERSHEY_DUPLEX
        print("PEYMAN Detected @", (x1,y1,x2,y2), datetime.datetime.now())
        cv2.putText(f, "PEYMAN", ( b2, a1+28), font, 1.0, (0, 255, 0), 1)
    


    cv2.imshow('IP Camera stream',f)
        


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cv2.destroyAllWindows()