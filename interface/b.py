from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QPlainTextEdit, QTabWidget
import sys

class NovaJanela(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Painel Secundário")
        self.setGeometry(200, 200, 600, 400)

        layout = QVBoxLayout()
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Adicionando widgets diferentes
        self.label = QLabel("📊 Painel de Controle Avançado")
        self.label.setStyleSheet("color: cyan; font-size: 18px; font-weight: bold;")

        self.log_area = QPlainTextEdit()
        self.log_area.setPlaceholderText("Área de Logs e Monitoramento...")
        self.log_area.setStyleSheet("background-color: #222; color: lime; font-family: monospace;")

        self.botao_atualizar = QPushButton("Atualizar Dados")
        self.botao_atualizar.clicked.connect(self.atualizar_logs)

        layout.addWidget(self.label)
        layout.addWidget(self.log_area)
        layout.addWidget(self.botao_atualizar)

    def atualizar_logs(self):
        self.log_area.appendPlainText("🔄 Dados atualizados com sucesso!")

class AssistenteUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Assistente Futurista")
        self.setGeometry(100, 100, 1200, 800)

        # Criando layout principal
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        self.configuracoes = QTabWidget()
        self.configuracoes.addTab(QWidget(), "Configuração")
        self.janelas_tab = QWidget()
        self.configuracoes.addTab(self.janelas_tab, "Janelas")

        layout.addWidget(self.configuracoes)

        # Botão para abrir nova janela personalizada
        janelas_layout = QVBoxLayout()
        self.janelas_tab.setLayout(janelas_layout)
        self.nova_janela_btn = QPushButton("Abrir Painel Secundário")
        self.nova_janela_btn.clicked.connect(self.abrir_painel_secundario)
        janelas_layout.addWidget(self.nova_janela_btn)

        # Lista para armazenar janelas abertas
        self.janelas_abertas = []

    def abrir_painel_secundario(self):
        nova_janela = NovaJanela()
        self.janelas_abertas.append(nova_janela)
        nova_janela.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = AssistenteUI()
    janela.show()
    sys.exit(app.exec())
