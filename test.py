import requests
import pyttsx3

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
    
    # Ajustar a taxa de fala
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 50)  # Reduzir a taxa de fala
    
    # Ajustar o volume
    volume = engine.getProperty('volume')
    engine.setProperty('volume', 1.0)  # Volume máximo
    
    # Selecionar uma voz diferente (opcional)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # Selecionar a voz com índice 1
    
    engine.say(text)
    engine.runAndWait()  # Espera a fala terminar
    engine.stop()  # Para o motor de fala corretamente

def main():
    print("Assistente ativada! Digite sua pergunta.")
    while True:
        user_input = input("Você: ")
        if user_input.lower() in ["sair", "exit", "quit"]:
            print("Encerrando...")
            break
        response = send_message_to_rasa(user_input)
        print(f"Assistente: {response}")
        speak(response)

if __name__ == "__main__":
    main()