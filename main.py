# -*- coding: utf-8 -*-

import os
import face_recognition
from PIL import Image, ImageFont, ImageDraw, ImageEnhance
# from tkinter import *
# from tkinter import ttk
from tkinter import filedialog




filepath = filedialog.askopenfilename()
#print(filepath)
# source = "./Untitled.png"
source = filepath
mil = face_recognition.load_image_file(source)
# Encoding Known faces

faces = []
encoded_faces = []
for filename in os.listdir("/home/peyman/PyMe/known"):
    if filename.endswith(".png") or filename.endswith(".jpg"): 
        path = f"/home/peyman/PyMe/known/{filename}"
        face = face_recognition.load_image_file(path)
        title = os.path.splitext(filename)[0]
        try:
            encoded_face = face_recognition.face_encodings(face)[0]
            faces.append(face)
            encoded_faces.append((encoded_face,title,False))
        except:
            pass



face_locations = face_recognition.face_locations(mil)

source_img = Image.open(source).convert("RGBA")
draw = ImageDraw.Draw(source_img)
for x1,y1,x2,y2 in face_locations:
    font = ImageFont.truetype("/home/peyman/PyMe/arial.ttf", 35, encoding="unic")
    point = ((y2,x2,y1,x1))
    print(point)
    a1 = max(x1,x2)
    b1 = max(y1,y2)
    a2 = min(x1,x2)
    b2 = min(y1,y2)    
    me = source_img.crop((b2,a2,b1,a1))
    me.save( "/home/peyman/PyMe/temp.png","PNG")

    unknown_picture = face_recognition.load_image_file("/home/peyman/PyMe/temp.png")
    unknown_face_encoding = face_recognition.face_encodings(unknown_picture)

    found = False
    try:
        for f,title,founded in encoded_faces:
            results = face_recognition.compare_faces([f], unknown_face_encoding[0],tolerance=0.5)
            if results[0] == True:
                draw.text((y2,x2),title,font=font,fill=(0,255,0))
                found = True
                break
        
        if(found == False):
                draw.text((y2,x2),"Unknown",font=font,fill=(255,0,0))
    except  IndexError:
        print("***"*555)


    draw.rectangle(((y1,x1),(y2,x2)), fill=None, outline=(0, 255, 0), width=7)

    

# source_img.save("output.png","PNG")
source_img.show()
print(len(face_locations))
