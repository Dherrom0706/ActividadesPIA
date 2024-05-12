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
    while(1):
        opcion = 0
        ret, frame = cap.read()

        if ret == True:
            k = cv2.waitKey(1) & 0xff
            if k == 27 or k == ord('q'):
                break 
            elif k == ord('1'):
                new_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
                cv2.imshow('Opcion1', new_frame)
            elif k == 2:
                new_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
                binr = cv2.threshold(new_frame, 197, 255, cv2.THRESH_BINARY)[1] 
                cv2.imshow('Opcion1', binr)
            elif k == 3:
                new_frame = frame
        cv2.imshow('Camshift',frame)  

        
    



    
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