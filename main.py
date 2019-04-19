import os 
import face_recognition 
from PIL import Image, ImageDraw, ImageFont
from tkinter import filedialog

source = filedialog.askopenfile()

image = face_recognition.load_image_file(source)
#Encoding Known faces in the ./known folder
encoded_faces=[] 
for filename in os.listdir("./known"): 
    if filename.endswith(".png") or filename.endswith(".jpg"):
        path=f"./known/{filename}" 
        face=face_recognition.load_image_file(path) 
        name=os.path.splitext(filename)[0]  #filename is the refrence for who is in the picture: Bill.jpg means Bill :)
        try:
            encoded_face = face_recognition.face_encodings(face)[0] # we know only 1 face is the known folder
            encoded_faces.append((encoded_face, name)) 
        except:   # if there is no face in the picture it couse error we ignore the error but there is nothing to do
            pass 

face_locations=face_recognition.face_locations(image) 
source_img = Image.open(source).convert("RGBA")

draw=ImageDraw.Draw(source_img)
for x1, y1, x2, y2 in face_locations: 
    font=ImageFont.Truetype("arial.ttf", 35, encoding="unic") 
    point=((y2, x2, y1, x1)) 
    a1=max(x1, x2) 
    b1=max(y1, y2) 
    a2=min(x1, x2) 
    b2=min(y1, y2) 
    me=source_img.crop((b2, a2, b1, a1)) 
    me.save("./temp.png","PNG") 
    unknown_picture=face_recognition.load_image_file("./temp.png") 
    unknown_face_encoding=face_recognition.face_encodings(unknown_picture) 
    found=False 
    try: 
        for face, name in encoded_faces: 
            results=face_recognition.compare_faces([face],unknown_face_encoding[o], tolerance=5) 
            if results[0]== True:
                draw.text((y2, x2), name, font=font, fill=(0,255, O)) 
                found=True
                break 

        if (found==False) : 
           draw.text((y2, x2),"Unknown", font=font, fill=(255, O, O)) 
    except IndexError:
        pass

    draw.rectangle (((y1, x1), (y2,x2) ), fill=None, outline=(0,255,0), width=7) 

#source_img.save("output. png","PNG") 
source_img.show()
print(f"Number of face(s):{len(face_locations)}")