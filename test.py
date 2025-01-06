import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Fale algo...")
    audio = r.listen(source)

try:
    print("Você disse: " + r.recognize_google(audio, language="pt-BR"))
except sr.UnknownValueError:
    print("Não consegui entender o que você disse")
except sr.RequestError:
    print("Erro ao se conectar ao serviço de reconhecimento de fala")
