import cv2
import numpy as np
#----------------------------------------------------------------------------
#Primer ejercicio
"""
Mostrar en la terminal el tamaño, número de canales y profundidad de canal de una
imagen cargada.
Copiar una imagen, usando otra imagen como máscara (las imágenes que se utilicen
como original y máscara tienen que tener el mismo tamaño. Todos los píxeles que
estén a cero en la imagen de máscara producirán un píxel negro en la imagen
copiada).
"""
imagen1 = cv2.imread("studysession\perrete.jpg")

#Total de pixeles incluyendo los canales
print("Tamaño total en pixeles contando los canales:",imagen1.size)
print("Pixeles y canales:",imagen1.shape)
print("Cantidad de canales:",imagen1.shape[2])
print("Profundidad:",imagen1.dtype) #Depth()

mascara = np.zeros(imagen1.shape[:2], np.uint8)
mascara[100:300, 100:600] = 255

#imagen_con_mascara = cv2.bitwise_and(imagen1,imagen1,mask = mascara)
imagen_con_mascara = cv2.copyTo(imagen1,mascara)

cv2.imshow('Mascara',mascara)
cv2.waitKey(0)
cv2.imshow('Imagen con la mascara',imagen_con_mascara)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Fin del primer ejercicio
#----------------------------------------------------------------------------

#----------------------------------------------------------------------------
#Segundo ejercicio
"""
Adaptar una imagen para invertir sus canales de tal forma que invierta los canales sólo
en un cierto rectángulo de la imagen. Concretamente, en el rectángulo cuya esquina
superior izquierda es el píxel en la fila 100, columna 100, y cuya esquina inferior
derecha es el píxel en la fila 300, columna 600 (por supuesto, se usará una imagen de
entrada de tamaño suficiente para poder definir este rectángulo).
"""

# for i in range (0,300):
#     for j in range (0,600):
#         for k in range (0,3):
#             if i >=100 and i<=300 and j>= 100 and j<=600:
#                 imagen1[i][j][k] = 255 - imagen1[i][j][k]

# cv2.imshow('Imagen con la inversión de los pixeles ',imagen1)
# cv2.waitKey(0)

#Fin del segundo ejercicio
#----------------------------------------------------------------------------

#----------------------------------------------------------------------------
#Tercer ejercicio
"""
Dada una imagen de entrada en niveles de gris deberá realizar lo siguiente:
    ● La suavice de cuatro maneras distintas, usando cada uno de los filtros explicados en esta Unidad.
    ● La binarice y la trunque.
    ● Detecte sus bordes usando el algoritmo de Canny.
Como tarea opcional, se hará un programa que ejecute los mismos pasos, pero que
acepte también, como entradas, imágenes en color (en este caso, el programa
internamente deberá convertir las imágenes de color a escala de grises, antes de
aplicarles los umbralizados y la detección de bordes).
"""

# imagen1 = cv2.imread("studysession\perrete.jpg")
# imagen_gris = cv2.cvtColor(imagen1, cv2.COLOR_BGR2GRAY) 

# # cv2.imshow('Imagen con la mascara',imagen_gris)
# # cv2.waitKey(0)

# cv2.imshow("Imagen con blur normal", cv2.blur(imagen_gris, (7,7)))
# cv2.waitKey(0)

# cv2.imshow("Imagen con blur de mediana", cv2.medianBlur(imagen_gris, 15))
# cv2.waitKey(0)

# cv2.imshow("Imagen con blur bilateral", cv2.bilateralFilter(imagen_gris, 15, 80, 80))
# cv2.waitKey(0)

# cv2.imshow("Imagen con blur gausiano", cv2.GaussianBlur(imagen_gris, (5,5), 2 ))
# cv2.waitKey(0)
#Fin del tercer ejercicio
#----------------------------------------------------------------------------

#----------------------------------------------------------------------------
#Cuarto ejercicio
"""
El alumno tendrá que escribir un programa de OpenCV que:
Rellene, en un mapa como el visto anteriormente, España de color rojo, Portugal
de verde, la zona de mar de azul y otro país (a elección del alumno) de otro
color cualquiera.
"""

# imagen4 = cv2.imread("studysession\mapa_garabateado.png")
  
# # Kernel a utilizar
# kernel = np.ones((3, 3), np.uint8) 

# #Todos los pixeles que pasan de 200 se ponen a blanco
# binr = cv2.threshold(imagen4, 197, 255, cv2.THRESH_BINARY)[1] 

# dilatacion = cv2.dilate(binr,kernel, iterations=2)

# final = cv2.erode(dilatacion, kernel, iterations=1)

# # opening the image 
# # imagen_open = cv2.morphologyEx(imagen4, cv2.MORPH_CLOSE, 
# #                            kernel, iterations=2) 

# cv2.imshow("Imagen procesada",final)
# cv2.waitKey(0)

# #Rellenado del mar

# cv2.floodFill(image=final, seedPoint=(1,1), newVal=(255,0,0), loDiff=(20,20,20), upDiff=(20,20,20), mask=None)

# #Rellenado de España
# cv2.floodFill(image=final, seedPoint=(40,215), newVal=(0,0,255), loDiff=(20,20,20), upDiff=(20,20,20), mask=None)

# #Rellenado de Portugal
# cv2.floodFill(image=final, seedPoint=(20,200), newVal=(0,255,0), loDiff=(20,20,20), upDiff=(20,20,20), mask=None)

# #Rellenado de Italia
# cv2.floodFill(image=final, seedPoint=(125,200), newVal=(0,255,255), loDiff=(20,20,20), upDiff=(20,20,20), mask=None)

# cv2.imshow("Imagen final ",final)
# cv2.waitKey(0)

#Fin del cuarto ejercicio
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
#Quinto ejercicio
"""
El alumno tendrá que escribir un programa de OpenCV que:
● Escriba, sobre una imagen, al menos una forma básica de cada color, y un texto.
"""

# imagen5 = cv2.imread("studysession\perrete.jpg")

# imagen = cv2.circle(imagen5, (735,230), radius=30,color=(14,120,255), thickness=6)
# imagen = cv2.ellipse(imagen, center=(735,120), axes=(20,100),color=(0,255,255), angle=90, startAngle=0, endAngle=360, thickness=12)
# imagen = cv2.rectangle(imagen, pt1=(600,280), pt2=(900,320), color=(255,255,255), thickness=10)
# imagen = cv2.line(imagen,(20,20), (300,500), color=(24,123,255), thickness = 25, lineType=9)
# imagen = cv2.putText(imagen, "Un buen chico con su juguete favorito :)", (200,50), color=(24,245,15), thickness=3, fontScale=1, fontFace=4)
# cv2.imshow("imagen",imagen)
# cv2.waitKey()
# Fin del quinto ejercicio
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
# Sexto ejercicio
"""
Utiliza la función selectROI con una imagen cualquiera donde aparezca alguna persona
y que saque por pantalla la imagen seleccionada. La parte de la imagen seleccionada
deberá salir difuminada con alguno de los métodos vistos en clase, por ejemplo, de
manera tal que anonimato.
Utiliza la función selectROIs con otra imagen distinta y que saque por pantalla las
imágenes seleccionadas. Aplica a cada una de las sub-imágenes un texto que
identifique esa sub-imagen.
"""

# roi = cv2.selectROI("Seleccione la zona de interes", imagen)
# imagen_recortada = imagen[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]
# cv2.imshow("Imagen con blur normal y recortada", cv2.blur(imagen_recortada, (30,30)))
# cv2.waitKey()

# rois = cv2.selectROIs("Seleccione todas las zonas de interes de la imagen", imagen)

# for i in range(0,len(rois)):
#     imagen_recortada_rois = imagen[int(rois[i][1]):int(rois[i][1]+rois[i][3]), int(rois[i][0]):int(rois[i][0]+rois[i][2])]
#     imagen_con_texto = cv2.putText(imagen_recortada_rois, str("imagen {0}".format(i)), (0,20), color=(24,0,255), thickness=2, fontScale=1, fontFace=4)
#     cv2.imshow("Imagen recortada",imagen_con_texto)
#     cv2.waitKey()
    
