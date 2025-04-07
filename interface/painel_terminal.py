# painel_terminal.py
from painel_base import PainelMovel
from PyQt5.QtWidgets import QLabel

class PainelTerminal(PainelMovel):
    def __init__(self):
        super().__init__("painel_terminal")
        self.setGeometry(50, 50, 400, 200)
        self.setStyleSheet("background-color: #1e1e1e; color: white;")
        label = QLabel("Terminal aqui", self)
        label.move(10, 10)
        self.restaurar_posicao()
