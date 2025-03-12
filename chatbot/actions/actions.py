import requests
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import json


class ActionSaudacaoComNome(Action):
    def name(self) -> str:
        return "action_saudacao_com_nome"

    def run(self, dispatcher, tracker, domain):
        nome = tracker.get_slot("nome")
        if nome:
            dispatcher.utter_message(text=f"Olá, {nome}! Como posso te ajudar hoje?")
        else:
            dispatcher.utter_message(text="Olá! Como posso te ajudar hoje?")
        return [SlotSet("nome", nome)]  # Garantir que o slot 'nome' seja mantido

class ActionCallGemma(Action):
    def name(self):
        return "action_call_gemma"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):
        user_message = tracker.latest_message.get("text")

        response = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": "gemma", "prompt": user_message}
        )

        print("Resposta da API:", response.text)  # <-- Adicione esta linha para debug

        if response.status_code == 200:
            responses = response.text.strip().split("\n")  # Divide a resposta em múltiplas linhas de JSON
            responses = [json.loads(r) for r in responses]  # Converte cada linha em um dicionário Python
            gemma_reply = " ".join([r.get("response", "") for r in responses])  # Junta todas as partes da resposta

        else:
            gemma_reply = "Erro ao se conectar com Gemma."

        dispatcher.utter_message(text=gemma_reply)
        return []
