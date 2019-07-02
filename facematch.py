import face_recognition

known_image = face_recognition.load_image_file('./img/known/Bill Gates.jpg')
known_face_encoding = face_recognition.face_encodings(known_image)[0]

unknown_image = face_recognition.load_image_file('./img/unknown/obama.jpeg')
unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]

# Compare faces
result = face_recognition.compare_faces([known_face_encoding], unknown_face_encoding)

print(result)
