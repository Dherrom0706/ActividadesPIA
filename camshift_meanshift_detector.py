import cv2
import numpy as np

"""
Método encargado de detectar pintar y devolver el frame con la cara con un recuadro según el metodo elegido y las 
posiciones pasadas por parametros

"""
def detectar_cara(x:int,y:int,w:int,h:int, metodo:int, frame):

    # Cogemos el roi de la cara desde el frame pasado, es decir donde se ha reconocido la cara
    roi_color = frame[y:y+h,x:x+w]

    # Recogemos el tamaño de la ventana
    track_window = (x, y, w, h)

    # Pasamos el roi a HSV
    hsv_roi = cv2.cvtColor(roi_color, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv_roi, np.array((0., 60.,32.)), np.array((180.,255.,255.)))
    roi_hist = cv2.calcHist([hsv_roi],[0],mask,[180],[0,180])
    cv2.normalize(roi_hist,roi_hist,0,255,cv2.NORM_MINMAX)
    # Setup the termination criteria, either 10 iteration or move by at least 1 pt
    term_crit = ( cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1 )

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    dst = cv2.calcBackProject([hsv],[0],roi_hist,[0,180],1)
    # apply camshift to get the new location
    if(metodo==0):
        ret2, track_window = cv2.CamShift(dst, track_window, term_crit)
        # Draw it on image
        pts = cv2.boxPoints(ret2)
        pts = np.int0(pts)
        img2 = cv2.polylines(frame,[pts],True, 255,2)
        return img2, track_window
    else:
        ret, track_window = cv2.meanShift(dst, track_window, term_crit)
        # Draw it on image
        x,y,w,h = track_window
        img2 = cv2.rectangle(frame, (x,y), (x+w,y+h), 255,2)
        return img2, track_window

# Modelo pre entrenado en cascada deteccion de caras y ojos
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
# Capturamos la webcam
cap = cv2.VideoCapture(0)

# Detect the faces

track_window = ()

while(1):
    ret, frame = cap.read()
    
    if (track_window == ()):
        faces= face_cascade.detectMultiScale(frame, 1.3, 5, minSize=(20,20), flags=cv2.CASCADE_SCALE_IMAGE)

    for (x, y, w, h) in faces:
   
        track_window_antigua = track_window
        frame, track_window  = detectar_cara(x, y, w, h, 0,frame)
        if(track_window_antigua == track_window):
            track_window = ()
    
    cv2.imshow('Camshift',frame)
    if ret == True:
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            cap.release()
            break 
    else:
        cap.release()
        break

cap.release()
cv2.destroyAllWindows()
cap = cv2.VideoCapture(0)

track_window = ()

while(1):
    ret, frame = cap.read()

    if (track_window == ()):
        faces = face_cascade.detectMultiScale(frame, 1.3, 5, minSize=(20,20), flags=cv2.CASCADE_SCALE_IMAGE)
    
    for (x, y, w, h) in faces:
        track_window_antigua = track_window
        frame, track_window = detectar_cara(x, y, w, h, 1,frame)
        if(track_window_antigua == track_window):
            track_window = ()

    cv2.imshow('MeanShift',frame)

    if ret == True:
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break 
    else:
        cap.release()
        break

