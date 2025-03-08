from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
import sys
import os

class AssistenteUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Assistente IA")
        self.setGeometry(100, 100, 800, 600)
        self.setObjectName("MainWindow")

        # Ativar modo maximizado ou tela cheia
        self.showMaximized()  # Ou self.showFullScreen()

        # Exemplo de um texto na tela
        self.label = QLabel("Olá, eu sou sua assistente!", self)
        self.label.setGeometry(50, 50, 400, 50)
        self.label.setObjectName("Titulo")
        self.label.show()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Carregar o QSS
    qss_file = os.path.join(os.path.dirname(__file__), "styles", "main.qss")
    if os.path.exists(qss_file):
        with open(qss_file, "r") as f:
            qss_content = f.read()
            print("QSS carregado:\n", qss_content)
            app.setStyleSheet(qss_content)

    janela = AssistenteUI()
    janela.show()
    sys.exit(app.exec())
