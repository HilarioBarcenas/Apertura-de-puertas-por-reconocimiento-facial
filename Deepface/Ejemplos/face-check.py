from traceback import print_stack
from deepface import DeepFace
print ("Se han comparado 2 imagenes. Verificación del individuo en proceso")
print ("Cargando...")

#result = DeepFace.verify(img1_path = "img1.jpg", img2_path = "img2.jpg")
result = DeepFace.verify(img1_path = "/home/hilario/Documentos/GitHub/Apertura-de-puertas-por-reconocimiento-facial/Deepface/Faces/Rumi.jpg", img2_path = "/home/hilario/Documentos/GitHub/Apertura-de-puertas-por-reconocimiento-facial/Deepface/Faces/Rumi2.jpg")

print ("Resultados: ")
print (result)