import face_recognition

picture_of_me = face_recognition.load_image_file("./known/mehdi.jpg")
my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]

# my_face_encoding now contains a universal 'encoding' of my facial features that can be compared to any other picture of a face!

unknown_picture = face_recognition.load_image_file("./sample/10.JPG")
unknown_face_encoding = face_recognition.face_encodings(unknown_picture)
face_locations = face_recognition.face_locations("./sample/10.JPG")


# Now we can see the two face encodings are of the same person with `compare_faces`!
for face in unknown_face_encoding:
    results = face_recognition.compare_faces([my_face_encoding], face)
    if results[0] == True:
        print("It's a picture of me!")
    else:
        print("It's not a picture of me!")
