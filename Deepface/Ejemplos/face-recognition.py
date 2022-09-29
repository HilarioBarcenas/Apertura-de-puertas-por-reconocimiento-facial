# Importar Bilbioteca
from deepface import DeepFace
import pandas as pd

# Buscar Rostro
print ("Buscando rostro")

# df = DeepFace.find(img_path = "img1.jpg", db_path = "C:/workspace/my_db")
#df = DeepFace.find (img_path = "/home/hugo/Documents/GitHub/apertura-puertas-reconocimiento-facial/deepface/faces/Rami.png", 
# db_path = "/home/hugo/Documents/GitHub/apertura-puertas-reconocimiento-facial/deepface/my_db", 
# enforce_detection = "false")
df = DeepFace.find (img_path = "/home/hilario/Documentos/GitHub/Apertura-de-puertas-por-reconocimiento-facial/Deepface/Faces/Dross.jpg", db_path = "/home/hilario/Documentos/GitHub/Apertura-de-puertas-por-reconocimiento-facial/Deepface/my_db", enforce_detection = "false")
print ("Resultado ")
print (df)
print ("Seleccion")
print (df.identity[0])