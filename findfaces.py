import face_recognition

# Load image as <class 'numpy.ndarray'>
image1 = face_recognition.load_image_file('./img/groups/team1.jpg')
face_locations1 = face_recognition.face_locations(image1)

image2 = face_recognition.load_image_file('./img/groups/team2.jpg')
face_locations2 = face_recognition.face_locations(image2)

# Array of coordinates (top, right, bottom, left) of each face
print(f'Coordinates of the face locations in team1.jpg - \n{face_locations1}')
print(f'There are {len(face_locations1)} people in team1.jpg\n')

print(f'Coordinates of the face locations in team1.jpg - \n{face_locations2}')
print(f'There are {len(face_locations2)} people in team1.jpg')
