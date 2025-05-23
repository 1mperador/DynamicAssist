from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from datetime import datetime
import subprocess
import os
import paramiko

# Configurações do servidor remoto
SSH_HOST = "192.1688.0.10"
SSH_USER = "leugim"
SSH_KEY = "/home/leugim/.ssh/id_rsa"

def executar_ssh(comando):
    cliente = paramiko.SSHClient()
    cliente.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    cliente.connect(hostname=SSH_HOST, username=SSH_USER, key_filename=SSH_KEY)
    stdin, stdout, stderr = cliente.exec_command(comando)
    saida = stdout.read().decode()
    erro = stderr.read().decode()
    cliente.close()
    return saida if saida else erro

class ActionDizerHora(Action):
    def name(self):
        return "action_dizer_hora"
    def run(self, dispatcher, tracker, domain):
        hora = datetime.now().strftime("%H:%M")
        dispatcher.utter_message(f"Agora são {hora}.")
        return []

class ActionDizerData(Action):
    def name(self):
        return "action_dizer_data"
    def run(self, dispatcher, tracker, domain):
        data = datetime.now().strftime("%d/%m/%Y")
        dispatcher.utter_message(f"Hoje é {data}.")
        return []

class ActionAbrirCalculadora(Action):
    def name(self):
        return "action_abrir_calculadora"
    def run(self, dispatcher, tracker, domain):
        subprocess.Popen(["gnome-calculator"])
        dispatcher.utter_message("Calculadora aberta.")
        return []

class ActionAbrirNavegador(Action):
    def name(self):
        return "action_abrir_navegador"
    def run(self, dispatcher, tracker, domain):
        subprocess.Popen(["xdg-open", "https://www.google.com"])
        dispatcher.utter_message("Abrindo o navegador.")
        return []

class ActionVerStatusServidor(Action):
    def name(self):
        return "action_ver_status_servidor"
    def run(self, dispatcher, tracker, domain):
        resultado = executar_ssh("uptime")
        dispatcher.utter_message(f"Status do servidor:\n{resultado}")
        return []

class ActionAtualizarSistema(Action):
    def name(self):
        return "action_atualizar_sistema"
    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Iniciando atualização remota...")
        resultado = executar_ssh("sudo apt update && sudo apt upgrade -y")
        dispatcher.utter_message(f"Atualização concluída:\n{resultado}")
        return []

class ActionReiniciarServidor(Action):
    def name(self):
        return "action_reiniciar_servidor"
    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Reiniciando o servidor remoto...")
        executar_ssh("sudo reboot")
        return []

class ActionVerificarTempo(Action):
    def name(self):
        return "action_verificar_tempo"
    def run(self, dispatcher, tracker, domain):
        # Exemplo usando o site wttr.in
        resultado = subprocess.getoutput("curl -s 'wttr.in/?format=3'")
        dispatcher.utter_message(f"Clima atual: {resultado}")
        return []

class ActionDizerHora(Action):
    def name(self):
        return "action_dizer_hora"
    def run(self, dispatcher, tracker, domain):
        from datetime import datetime
        hora = datetime.now().strftime("%H:%M")
        dispatcher.utter_message(f"Agora são {hora}.")
        return []

class ActionAbrirCalculadora(Action):
    def name(self):
        return "action_abrir_calculadora"
    def run(self, dispatcher, tracker, domain):
        os.system("gnome-calculator &")
        dispatcher.utter_message("Calculadora aberta!")
        return []

# import requests
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
# from rasa_sdk.events import SlotSet
# import json
# import os

# class ActionSaudacaoComNome(Action):
#     def name(self) -> str:
#         return "action_saudacao_com_nome"

#     def run(self, dispatcher, tracker, domain):
#         nome = tracker.get_slot("nome")
#         if nome:
#             dispatcher.utter_message(text=f"Olá, {nome}! Como posso te ajudar hoje?")
#         else:
#             dispatcher.utter_message(text="Olá! Como posso te ajudar hoje?")
#         return [SlotSet("nome", nome)]  # Garantir que o slot 'nome' seja mantido

# class ActionCallGemma(Action):
#     def name(self):
#         return "action_call_gemma"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):
#         user_message = tracker.latest_message.get("text")

#         response = requests.post(
#             "http://localhost:11434/api/generate",
#             json={"model": "gemma", "prompt": user_message}
#         )

#         print("Resposta da API:", response.text)  # <-- Adicione esta linha para debug

#         if response.status_code == 200:
#             responses = response.text.strip().split("\n")  # Divide a resposta em múltiplas linhas de JSON
#             responses = [json.loads(r) for r in responses]  # Converte cada linha em um dicionário Python
#             gemma_reply = " ".join([r.get("response", "") for r in responses])  # Junta todas as partes da resposta

#         else:
#             gemma_reply = "Erro ao se conectar com Gemma."

#         dispatcher.utter_message(text=gemma_reply)
#         return []


