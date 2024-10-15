# There is a problem to install the module face recognition in my laptop that's why currently 
# i can not run this code but you can try it in your laptop.

import cv2 as cv
import face_recognition
import matplotlib.pyplot as plt

known_image = face_recognition.load_image_file("Saurav.jpeg")
known_faces = face_recognition.face_encodings(known_image, num_jitters=50, model='large')[0]

cam = cv.VideoCapture(0)

if not cam.isOpened():
    print("Camera not working")
    exit()

while True:
    ret, frame = cam.read()

    if not ret:
        print("Can't receive the frame")
        break

    face_locations = face_recognition.face_locations(frame)

    for face_location in face_locations:
        top, right, bottom, left = face_location
        cv.rectangle(frame, (left, top), (right, bottom), color=(0, 0, 255), thickness=2)

    face_encodings = face_recognition.face_encodings(frame, num_jitters=23, model='large')

    if face_encodings:
        Live_face_encoding = face_encodings[0]
        results = face_recognition.compare_faces([known_faces], Live_face_encoding)

        if results[0]:
            img = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
            img = cv.putText(img, 'Saurav', (30, 55), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv.LINE_AA)
            print('Saurav Chaudhary Enter....')
            plt.imshow(img)
            plt.show()
            break
    else:
        img = cv.putText(frame, 'Not Saurav', (30, 55), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv.LINE_AA)
        cv.imshow('frame', img)

    if cv.waitKey(1) == ord('q'):
        break

cam.release()
cv.destroyAllWindows()