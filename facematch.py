import face_recognition

known_image = face_recognition.load_image_file('./img/known/Bill Gates.jpg')
known_face_encoding = face_recognition.face_encodings(known_image)
