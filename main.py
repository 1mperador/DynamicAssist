import requests
import pyttsx3
import readline
import subprocess
import os
import paramiko
import speech_recognition as sr
from termcolor import colored

def send_message_to_rasa(message):
    url = "http://localhost:5005/webhooks/rest/webhook"
    payload = {"sender": "user", "message": message}
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        responses = response.json()
        if responses:
            return responses[0].get("text", "Desculpe, não entendi.")
    return "Erro ao comunicar com a Rasa."

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 130)
    engine.setProperty('volume', 1.0)
    voices = engine.getProperty('voices')
    for voice in voices:
        if "brazil" in voice.id.lower():
            engine.setProperty('voice', voice.id)
            break
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def ouvir_comando():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        print(colored("🎙️  Ouvindo... Fale agora.", "yellow"))
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        comando = recognizer.recognize_google(audio, language="pt-BR")
        print(colored(f"Você disse: {comando}", "blue"))
        return comando
    except sr.UnknownValueError:
        print(colored("Não entendi o que você disse.", "red"))
        return ""
    except sr.RequestError:
        print(colored("Erro ao acessar o serviço de reconhecimento de voz.", "red"))
        return ""

def executar_comando_remoto(comando):
    host = "192.168.0.10"  # Substitua pelo IP do seu servidor
    usuario = "leugim"  # Ex: ubuntu
    caminho_chave = "/home/leugim/.ssh/id_rsa"

    try:
        cliente = paramiko.SSHClient()
        cliente.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        cliente.connect(hostname=host, username=usuario, key_filename=caminho_chave)

        stdin, stdout, stderr = cliente.exec_command(comando)
        saida = stdout.read().decode()
        erro = stderr.read().decode()
        cliente.close()
        return saida if saida else erro
    except Exception as e:
        return f"Erro ao conectar ao servidor: {str(e)}"

def main():
    print(colored("\n=================================", "cyan"))
    print(colored("     WEL COME ALGUEM", "green"))
    print(colored("=================================\n", "cyan"))
    print(colored("Fale ou digite sua pergunta. Diga ou digite 'sair' para encerrar.", "yellow"))
    
    while True:
        print(colored("\n[1] Falar\n[2] Digitar\nEscolha uma opção:", "cyan"), end=" ")
        modo = input()

        if modo == "1":
            user_input = ouvir_comando()
        else:
            user_input = input(colored("\nVocê: ", "blue"))

        if user_input.lower() in ["sair", "exit", "quit"]:
            print(colored("Encerrando...", "red"))
            speak("Encerrando o sistema.")
            break

        if user_input.strip() == "":
            continue

        # Lógica para detectar comandos SSH personalizados
        if "servidor" in user_input or "remoto" in user_input:
            if "atualizar" in user_input:
                resposta = executar_comando_remoto("sudo apt update && sudo apt upgrade -y")
            elif "uso do disco" in user_input:
                resposta = executar_comando_remoto("df -h")
            elif "tempo ligado" in user_input or "uptime" in user_input:
                resposta = executar_comando_remoto("uptime")
            else:
                resposta = "Comando remoto não reconhecido."
        else:
            resposta = send_message_to_rasa(user_input)

        print(colored(f"Assistente: {resposta}", "magenta"))
        speak(resposta)

if __name__ == "__main__":
    main()
