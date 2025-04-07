# painel_menu.py
from PyQt5.QtWidgets import QFrame, QPushButton
from PyQt5.QtCore import Qt

class MenuControle(QFrame):
    def __init__(self, parent, paineis):
        super().__init__(parent)
        self.paineis = paineis
        self.setGeometry(10, 10, 200, 120)
        self.setStyleSheet("background-color: #FFFFFF; border: 2px solid #555; border-radius: 10px;")

        btn_mostrar = QPushButton("Mostrar Todos", self)
        btn_mostrar.setGeometry(20, 10, 160, 30)
        btn_mostrar.clicked.connect(self.mostrar_todos)

        btn_ocultar = QPushButton("Ocultar Todos", self)
        btn_ocultar.setGeometry(20, 45, 160, 30)
        btn_ocultar.clicked.connect(self.ocultar_todos)

        btn_restaurar = QPushButton("Restaurar Posições", self)
        btn_restaurar.setGeometry(20, 80, 160, 30)
        btn_restaurar.clicked.connect(self.restaurar_posicoes)

    def mostrar_todos(self):
        for p in self.paineis:
            p.show()

    def ocultar_todos(self):
        for p in self.paineis:
            p.hide()

    def restaurar_posicoes(self):
        for p in self.paineis:
            p.restaurar_posicao()
