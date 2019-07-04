import face_recognition
from PIL import Image, ImageDraw

image_of_bill = face_recognition.load_image_file('img/known/Bill Gates.jpg')
bill_faec_encoding = face_recognition.face_encodings(image_of_bill)[0]

image_of_steve = face_recognition.load_image_file('img/known/Steve Jobs.png')
steve_face_encoding = face_recognition.face_encodings(image_of_steve)[0]
