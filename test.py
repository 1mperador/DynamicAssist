import requests
import pyttsx3
import readline
from termcolor import colored
import subprocess
import os

def send_message_to_rasa(message):
    url = "http://localhost:5005/webhooks/rest/webhook"  # URL do servidor Rasa
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

def main():
    print(colored("\n=================================", "cyan"))
    print(colored("     ASSISTENTE VIRTUAL IA", "green"))
    print(colored("=================================\n", "cyan"))
    print(colored("Digite sua pergunta ou 'sair' para encerrar.", "yellow"))
    
    while True:
        user_input = input(colored("\nVocê: ", "blue"))
        if user_input.lower() in ["sair", "exit", "quit"]:
            print(colored("Encerrando...", "red"))
            speak("Encerrando o sistema.")
            break
        response = send_message_to_rasa(user_input)
        print(colored(f"Assistente: {response}", "magenta"))
        speak(response)

if __name__ == "__main__":
    main()
