# Actividad
# Prueba ambos algoritmos de flujo óptico vistos en la página anterior e intenta modificar
# los parámetros para mejorar los resultados. Puedes usar la cámara frontal de tu portátil
# o algún video sacado de internet (por ejemplo, coches circulando por la carretera).

import numpy as np
import cv2 as cv

cap = cv.VideoCapture("slow_traffic_small.mp4")
# params for ShiTomasi corner detection
#Cambio a 2 - 2 toma mas puntos de referencia en las esquinas ya que la distancia y el bloque a coger es menor
# Cambiando max corners hacemos que pueda tener mas puntos cogidos al mismo tiempo
feature_params = dict( maxCorners = 200,qualityLevel = 0.3,minDistance = 2,blockSize = 2 )
# Parameters for lucas kanade optical flow
lk_params = dict( winSize = (15, 15),maxLevel = 2, criteria = (cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 0.03))
# Create some random colors
color = np.random.randint(0, 255, (100, 3))
# Take first frame and find corners in it
ret, old_frame = cap.read()
old_gray = cv.cvtColor(old_frame, cv.COLOR_BGR2GRAY)
p0 = cv.goodFeaturesToTrack(old_gray, mask = None, **feature_params)
# Create a mask image for drawing purposes
mask = np.zeros_like(old_frame)
while(1):
    ret, frame = cap.read()
    if not ret:
        print('No frames grabbed!')
        break
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # calculate optical flow
    p1, st, err = cv.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)
    # Select good points
    if p1 is not None:
        good_new = p1[st==1]
        good_old = p0[st==1]
    # draw the tracks
    for i, (new, old) in enumerate(zip(good_new, good_old)):
        a, b = new.ravel()
        c, d = old.ravel()
        mask = cv.line(mask, (int(a), int(b)), (int(c), int(d)), color[i].tolist(), 2)
        frame = cv.circle(frame, (int(a), int(b)), 5, color[i].tolist(), -1)
        img = cv.add(frame, mask)
    cv.imshow('frame', img)
    k = cv.waitKey(30) & 0xff
    if k == 27:
        break
    # Now update the previous frame and previous points
    old_gray = frame_gray.copy()
    p0 = good_new.reshape(-1, 1, 2)
cv.destroyAllWindows()