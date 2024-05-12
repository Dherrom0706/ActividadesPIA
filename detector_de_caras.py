"""
El alumno tendrá que escribir un programa de OpenCV que:
● Detecte caras en una imagen, marque esas caras como regiones de interés
(ROI) y, SÓLO EN ESAS REGIONES DE INTERÉS, detecte ojos. La salida del
programa mostrará la imagen original, con rectángulos sobreescritos de
diferentes colores para indicar las caras y ojos detectados, como muestra la
figura anterior.
● Usa el clasificador de sonrisas que viene en OpenCV y escribe un programa que
detecte sonrisas en una imagen de un grupo de amigo/as sonrientes.
"""

import cv2
import numpy as np
# Modelo pre entrenado en cascada deteccion de caras y ojos
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')
# Capturamos la webcam
cap = cv2.VideoCapture(0)

while True:
    # Read the frame
    _, img = cap.read()
    # Convert to grayscale

    kernel = np.ones((3, 3), np.uint8) 

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Aclarar la imagen si falta luz
    dilatacion = cv2.dilate(gray,kernel, iterations=3)

    # Detect the faces
    faces = face_cascade.detectMultiScale(dilatacion, 1.3, 5, minSize=(30,30), flags=cv2.CASCADE_SCALE_IMAGE)
    
    # Draw the rectangle around each face
    for (x, y, w, h) in faces:

        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

        roi_gray = gray[y:y+h,x:x+w]
        roi_color = img[y:y+h,x:x+w]

        eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 5, minSize=(30,30), flags=cv2.CASCADE_SCALE_IMAGE)
        
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,255),2)

        smile = smile_cascade.detectMultiScale(roi_gray, 1.3, 5, minSize=(30,30),flags=cv2.CASCADE_SCALE_IMAGE)

        for (ex,ey,ew,eh) in smile:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

    # Display   
    cv2.imshow('img', img)
    # Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
# Release the VideoCapture object
cap.release()