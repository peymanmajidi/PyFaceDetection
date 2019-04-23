"""Access IP Camera in Python OpenCV"""

import cv2
import face_recognition
from PIL import Image, ImageFont, ImageDraw, ImageEnhance
import os,numpy


stream = cv2.VideoCapture('rtsp://admin:12345@192.168.2.180/1')  



encoded_faces = []
names = []
for filename in os.listdir("/home/peyman/PyMe/known"):
    if filename.endswith(".png") or filename.endswith(".jpg"): 
        path = f"/home/peyman/PyMe/known/{filename}"
        face = face_recognition.load_image_file(path)
        title = os.path.splitext(filename)[0]
        try:
            encoded_face = face_recognition.face_encodings(face)[0]
            encoded_faces.append(encoded_face)
            names.append(title)
        except:
            pass


while True:
    r, f = stream.read()
    small_frame = cv2.resize(f, (0, 0), fx=0.25, fy=0.25)
    mil = small_frame[:, :, ::-1]
    face_locations = face_recognition.face_locations(mil)
    face_encodings = face_recognition.face_encodings(mil, face_locations)

    face_names = []
    
    for face_encoding in face_encodings:
        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(encoded_faces, face_encoding)
        name = "Unknown"

        # If a match was found in known_face_encodings, just use the first one.
        if True in matches:
            first_match_index = matches.index(True)
            name = names[first_match_index]

        face_names.append(name)




    for (x1,y1,x2,y2),n in zip(face_locations,names):
        a1 = max(x1,x2)*4
        b1 = max(y1,y2)*4
        a2 = min(x1,x2)*4
        b2 = min(y1,y2)*4  

        cv2.rectangle(f, (b2, a2),( b1, a1), (0, 255, 0), 5)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(f, title, ( b2, a1+28), font, 1.0, (0, 255, 0), 1)

    cv2.imshow('IP Camera stream',f)
        


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cv2.destroyAllWindows()