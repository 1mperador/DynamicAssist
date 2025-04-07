# painel_base.py
from PyQt5.QtWidgets import QFrame, QPushButton
from PyQt5.QtCore import Qt, QPoint, QSettings

class PainelMovel(QFrame):
    def __init__(self, nome_unico, parent=None):
        super().__init__(parent)
        self.nome_unico = nome_unico
        self._drag_active = False
        self._drag_position = QPoint()
        self.setFrameShape(QFrame.StyledPanel)
        self.setStyleSheet("background-color: #222; border: 2px solid #555; border-radius: 10px;")
        self.setWindowFlags(Qt.Widget | Qt.FramelessWindowHint)

        # Botão de fechar
        self.btn_fechar = QPushButton("×", self)
        self.btn_fechar.setGeometry(self.width() - 25, 5, 20, 20)
        self.btn_fechar.setStyleSheet("background-color: red; color: white; border: none;")
        self.btn_fechar.clicked.connect(self.hide)
        self.btn_fechar.raise_()  # Garante que fique visível

    def resizeEvent(self, event):
        # Garante que o botão fique no canto sempre
        self.btn_fechar.move(self.width() - 30, 5)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self._drag_active = True
            self._drag_position = event.globalPos() - self.pos()
            event.accept()

    def mouseMoveEvent(self, event):
        if self._drag_active:
            self.move(event.globalPos() - self._drag_position)
            event.accept()

    def mouseReleaseEvent(self, event):
        self._drag_active = False
        self.salvar_posicao()

    def salvar_posicao(self):
        settings = QSettings("MinhaAssistente", "PainelPosicoes")
        settings.setValue(self.nome_unico, self.pos())

    def restaurar_posicao(self):
        settings = QSettings("MinhaAssistente", "PainelPosicoes")
        pos = settings.value(self.nome_unico)
        if pos:
            self.move(pos)
