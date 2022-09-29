from deepface import DeepFace
obj = DeepFace.analyze(img_path = "/home/hilario/Documentos/GitHub/Apertura-de-puertas-por-reconocimiento-facial/Deepface/Faces/Rumi.jpg", 
        actions = ['age', 'gender', 'race', 'emotion']
)
print ("El resultado del analisis es: ")
print (obj)