# main.py
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from painel_terminal import PainelTerminal
from painel_btop import PainelBtop
from painel_vazio import PainelVazio
from painel_menu import MenuControle

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Interface da Assistente")
        self.setGeometry(100, 100, 1000, 600)

        self.painel_terminal = PainelTerminal()
        self.painel_btop = PainelBtop()
        self.painel_vazio = PainelVazio()

        # self.painel_terminal.setParent(self)
        # self.painel_btop.setParent(self)
        # self.painel_vazio.setParent(self)

        # self.painel_terminal.show()
        # self.painel_btop.show()
        # self.painel_vazio.show()

        self.paineis = [
            self.painel_terminal,
            self.painel_btop,
            self.painel_vazio
        ]

        for painel in self.paineis:
            painel.setParent(self)
            painel.show()

        self.menu_controle = MenuControle(self, self.paineis)
        self.menu_controle.show()

        self.showFullScreen()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setOrganizationName("MinhaAssistente")
    app.setApplicationName("PainelPosicoes")
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
