import cv2
import os

# Crie uma pasta para salvar as imagens
if not os.path.exists('fotos'):
    os.makedirs('fotos')

# Inicialize a webcam
camera = cv2.VideoCapture(0)

# Use o classificador Haar Cascade pré-treinado do OpenCV
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Número de imagens para capturar
num_images = 20
count = 0

print("Posicione-se na frente da câmera. Pressione 'q' para sair a qualquer momento.")

while True:
    ret, frame = camera.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Desenhar retângulos em torno dos rostos detectados
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # Salvar a imagem do rosto detectado
        face = gray[y:y+h, x:x+w]
        cv2.imwrite(f"fotos/face_{count}.jpg", face)
        count += 1

        # Pare após capturar o número necessário de imagens
        if count >= num_images:
            print("Imagens capturadas.")
            camera.release()
            cv2.destroyAllWindows()
            exit()

    cv2.imshow("Captura de Rostos", frame)

    # Saia com a tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
