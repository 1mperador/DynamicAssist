import cv2
import sounddevice as sd
import numpy as np
import threading
import speech_recognition as sr
import json
import pyttsx3
import pyaudio
from time import sleep

# Função para carregar falas do arquivo JSON
def carregar_falas():
    with open("fala.json", "r") as file:
        return json.load(file)

# Função para fazer a assistente falar
def falar(mensagem):
    engine = pyttsx3.init()
    engine.say(mensagem)
    engine.runAndWait()

# Função para escutar o comando de voz
def ouvir_comando():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Ajustando para o ambiente...")
        r.adjust_for_ambient_noise(source)
        print("Ouvindo...")
        audio = r.listen(source)

    try:
        comando = r.recognize_google(audio, language='pt-BR')
        print(f"Você disse: {comando}")
        return comando.lower()
    except sr.UnknownValueError:
        print("Não entendi o que você disse")
        return ""
    except sr.RequestError:
        print("Erro ao se conectar ao serviço de reconhecimento de fala")
        return ""


# Função para detectar rosto
def detectar_rosto(recognizer, face_cascade):
    global rosto_detectado
    camera = cv2.VideoCapture(0)
    while True:
        ret, frame = camera.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(100, 100))

        for (x, y, w, h) in faces:
            face_id, confidence = recognizer.predict(gray[y:y+h, x:x+w])
            if confidence < 60:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                cv2.putText(frame, "Usuario detectado", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
                rosto_detectado = True  # Ativa o sinal de rosto detectado

        cv2.imshow("Video", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    camera.release()
    cv2.destroyAllWindows()

# Função para detectar áudio (som)
def detectar_audio(limiar=0.01, duracao=1):
    global rosto_detectado
    while True:
        if rosto_detectado:
            print("Analisando som...")
            audio = sd.rec(int(duracao * 44100), samplerate=44100, channels=1, dtype='float64')
            sd.wait()
            if np.max(np.abs(audio)) > limiar:
                print("Usuário falando! Assistente ativada.")
                # Aqui você chama o reconhecimento de fala ou outro processo
                comando = ouvir_comando()  # Chama a função de comando de voz quando o som é detectado
                print(f"Comando detectado: {comando}")  # Adiciona um print para verificar o comando
                if "oi" in comando:
                    falar(falas["oi"])
                elif "boa tarde" in comando:
                    falar(falas["boa_tarde"])
                elif "tchau" in comando:
                    falar(falas["despedida"])
                    break
                sleep(5)  # Evita novas ativações imediatamente
            rosto_detectado = False  # Reseta o sinal para o próximo ciclo
        else:
            sleep(0.5)  # Aguarda para verificar o rosto novamente


# Função principal para configurar e iniciar os threads
def main():
    global rosto_detectado, falas
    falas = carregar_falas()

    # Carregar o classificador de rosto e modelo de reconhecimento
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read("modelo.yml")

    rosto_detectado = False

    # Criação de threads para rosto e som
    thread_rosto = threading.Thread(target=detectar_rosto, args=(recognizer, face_cascade))
    thread_audio = threading.Thread(target=detectar_audio)

    thread_rosto.start()
    thread_audio.start()

    thread_rosto.join()
    thread_audio.join()

if __name__ == "__main__":
    main()
