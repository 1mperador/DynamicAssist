# painel_terminal.py
from painel_base import PainelMovel
from PyQt5.QtWidgets import QLabel

class PainelVazio(PainelMovel):
    def __init__(self):
        super().__init__("painel_vazio")
        self.setGeometry(50, 50, 400, 200)
        self.setStyleSheet("background-color: #1e1e1e; color: white;")
        label = QLabel("Painel vazio", self)
        label.move(10, 10)
        self.restaurar_posicao()
