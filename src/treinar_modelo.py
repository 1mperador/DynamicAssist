import cv2
import os
import numpy as np

# Inicialize o reconhecedor de faces
recognizer = cv2.face.LBPHFaceRecognizer_create()

# Diretório com as imagens
path = 'fotos'

# Carregar as imagens e os rótulos
faces = []
labels = []
for file in os.listdir(path):
    if file.endswith('.jpg'):
        img = cv2.imread(f"{path}/{file}", cv2.IMREAD_GRAYSCALE)
        faces.append(np.array(img, dtype='uint8'))
        labels.append(1)  # Rotulo 1 (pode ajustar para múltiplas pessoas no futuro)

# Treinar o modelo
recognizer.train(faces, np.array(labels))
recognizer.save("modelo.yml")
print("Modelo treinado e salvo como 'modelo.yml'.")
