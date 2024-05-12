"""
El alumno tendrá que escribir un programa de OpenCV que procese los fotogramas de
una secuencia de vídeo de la siguiente manera:
    ● Si no se pulsa ninguna tecla, no se hará procesado alguno.
    ● Si se pulsa la tecla '1', el programa convertirá cada fotograma a escala de grises
    (nota: usar la función cvtColor, por ejemplo cvtColor(frame, frame_proc,
    CV_BGR2GRAY); carga en frame_proc la versión en escala de grises de frame).
    ● Si se pulsa la tecla '2', el programa convertirá cada fotograma a escala de grises
    y luego lo binarizará con la función threshold.
    ● Al pulsar la tecla '3', el programa vuelve a su comportamiento original, y no
    habrá procesado alguno con los fotogramas.
    ● Las teclas 'q', 'Q' o 'Esc' detienen la ejecución del programa.
Para cada fotograma, el programa representará el fotograma original y el resultado del
procesado. El código se elaborará usando un único archivo .py
"""

import cv2
import numpy as np


cap = cv2.VideoCapture(0)
def main():
    
    opcion = 0
    while(1):
        ret, frame = cap.read()
        ret, frame2 = cap.read()
        if ret == True:
            k = cv2.waitKey(1) & 0xff
            if k == 27 or k == ord('q'):
                break 
            elif k == ord('1'):
                opcion = 1
            elif k == ord('2'):
                opcion = 2
            elif k == ord('3'):
                opcion = 3
        if opcion == 1:
            frame2 = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        if opcion == 2:
            frame2 = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            frame2 = cv2.threshold(frame2, 197, 255, cv2.THRESH_BINARY)[1]
        if opcion == 3:
            frame2 = frame
        cv2.imshow('Opcion elegida', frame2)
        cv2.imshow('Camara base',frame)  

        
    



    
def pedir_opcion():
    print("Teclee una de las siguientes opciones:") 
    print("1.- Se convertirá el video a escala de grises")
    print("2.- Se convertirá el video a escala de grises y se hará una binarización")
    print("3.- Se mostrará el video original")
    try:
        opcion = int(input("Opción: "))
        while(opcion < 1 or opcion > 3):
            opcion = input("Inserte una opción correcta: ")

        return opcion
    except Exception:
        print("Es necesario que introduzca una opción valida")
        return 0
    
    
    

if __name__ == "__main__":
    main()