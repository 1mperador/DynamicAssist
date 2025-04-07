from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QGridLayout, QTreeView, QTextEdit, QPlainTextEdit, QPushButton, QGroupBox, QHBoxLayout, QLabel, QTabWidget, QDialog
from PyQt6.QtGui import QFileSystemModel
from PyQt6.QtCore import QProcess, QIODevice
import sys
import os

class NovaJanela(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Nova Janela")
        self.setGeometry(100, 100, 600, 400)
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.editor = QTextEdit()
        layout.addWidget(self.editor)

class AssistenteUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Assistente Futurista")
        self.setGeometry(100, 100, 1200, 800)
        
        # Criando o layout principal
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QGridLayout()
        central_widget.setLayout(layout)
        
        # Coluna da esquerda
        left_column = QVBoxLayout()
        
        # Seção 5: Terminal (colocado no topo)
        self.terminal = QPlainTextEdit()
        self.terminal.setPlaceholderText("Digite comandos para a assistente...")
        self.terminal.setFixedHeight(200)  # Ajustando a altura do terminal
        left_column.addWidget(self.terminal)
        
        # Espaço entre o terminal e os arquivos
        left_column.addSpacing(20)
        
        # Seção 1: Arquivos reais
        self.modelo_arquivos = QFileSystemModel()
        self.modelo_arquivos.setRootPath(os.path.expanduser("~/Documentos/GitHub"))  # Diretório inicial
        
        self.arquivos = QTreeView()
        self.arquivos.setModel(self.modelo_arquivos)
        self.arquivos.setRootIndex(self.modelo_arquivos.index(os.path.expanduser("~/Documentos/GitHub")))
        self.arquivos.setMaximumHeight(200)  # Ajustando a altura
        
        left_column.addWidget(self.arquivos)
        
        # Seção 2: Configurações
        self.configuracoes = QTabWidget()
        self.configuracoes.addTab(QWidget(), "Layout")
        self.janelas_tab = QWidget()
        self.configuracoes.addTab(self.janelas_tab, "Janelas")
        self.configuracoes.setMaximumHeight(150)  # Ajustando a altura para ser menor que os arquivos
        self.configuracoes.setStyleSheet(
            "QTabWidget::pane { border: 1px solid gray; }"
            "QTabBar::tab { background: #555; color: white; padding: 5px; }"
            "QTabBar::tab:selected { background: #777; }"
        )
        left_column.addWidget(self.configuracoes)
        
        layout.addLayout(left_column, 0, 0, 3, 1)
        
        # Espaço entre as colunas
        layout.setColumnMinimumWidth(1, 20)
        
        # Coluna da direita
        right_column = QVBoxLayout()
        
        # Seção 4: Visualização (movida para o topo direito)
        self.visualizacao = QLabel("Visualização")
        self.visualizacao.setStyleSheet("background-color: #444; color: white; text-align: center;")
        self.visualizacao.setFixedSize(200, 200)  # Definindo como um quadrado
        right_column.addWidget(self.visualizacao)
        
        # Espaço entre visualização e diagnóstico
        right_column.addSpacing(20)
        
        # Seção 3: Diagnóstico
        self.diagnostico = QPlainTextEdit()
        self.diagnostico.setPlaceholderText("Logs e notificações...")
        self.diagnostico.setReadOnly(True)
        self.diagnostico.setFixedHeight(200)  # Ajustando a altura do diagnóstico
        right_column.addWidget(self.diagnostico)
        
        # Adicionando o terminal literal
        self.terminal_process = QProcess(self)
        self.terminal_process.setProgram('bash')
        self.terminal_process.setArguments(['-c', 'tail -f /var/log/syslog'])  # Exemplo de comando para mostrar logs
        self.terminal_process.setProcessChannelMode(QProcess.ProcessChannelMode.MergedChannels)
        self.terminal_process.readyReadStandardOutput.connect(self.update_terminal)
        self.terminal_process.start()
        
        layout.addLayout(right_column, 0, 2, 3, 1)
        
        # Adicionando botão para criar nova janela na aba "Janelas"
        janelas_layout = QVBoxLayout()
        self.janelas_tab.setLayout(janelas_layout)
        self.nova_janela_btn = QPushButton("Criar Nova Janela")
        self.nova_janela_btn.clicked.connect(self.criar_nova_janela)
        janelas_layout.addWidget(self.nova_janela_btn)
        
        # Aplicando estilos básicos
        self.setStyleSheet(
            "QTreeView { background-color: #222; color: white; padding: 5px; }"
            "QTextEdit { background-color: #111; color: #0f0; font-family: monospace; }"
            "QPlainTextEdit { background-color: #000; color: #0f0; font-family: monospace; }"
            "QLabel { background-color: #444; color: white; text-align: center; }"
            "QWidget { background-color: #333; }"
            "QPushButton { background-color: #555; color: white; padding: 5px; border-radius: 5px; }"
            "QGroupBox { background-color: #222; color: white; border: 1px solid gray; padding: 5px; }"
        )

    def criar_nova_janela(self):
        nova_janela = AssistenteUI()
        nova_janela.show()

    def update_terminal(self):
        output = self.terminal_process.readAllStandardOutput().data().decode()
        self.diagnostico.appendPlainText(output)

    def closeEvent(self, event):
        self.terminal_process.terminate()
        self.terminal_process.waitForFinished()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = AssistenteUI()
    janela.show()
    sys.exit(app.exec())
    

# from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QGridLayout, QTreeView, QTextEdit, QPlainTextEdit, QPushButton, QGroupBox, QHBoxLayout, QLabel, QTabWidget, QDialog
# from PyQt6.QtGui import QFileSystemModel
# from PyQt6.QtCore import QProcess, QIODevice
# import sys
# import os

# class AssistenteUI(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Assistente Futurista")
#         self.setGeometry(100, 100, 1200, 800)

#         # Criando o layout principal
#         central_widget = QWidget()
#         self.setCentralWidget(central_widget)
#         layout = QGridLayout()
#         central_widget.setLayout(layout)

#         # Coluna da esquerda
#         left_column = QVBoxLayout()

#         # Seção 5: Terminal (colocado no topo)
#         self.terminal = QPlainTextEdit()
#         self.terminal.setPlaceholderText("Digite comandos para a assistente...")
#         self.terminal.setFixedHeight(200)  # Ajustando a altura do terminal
#         left_column.addWidget(self.terminal)

#         # Espaço entre o terminal e os arquivos
#         left_column.addSpacing(20)

#         # Seção 1: Arquivos reais
#         self.modelo_arquivos = QFileSystemModel()
#         self.modelo_arquivos.setRootPath(os.path.expanduser("~/Documentos/GitHub"))  # Diretório inicial
        
#         self.arquivos = QTreeView()
#         self.arquivos.setModel(self.modelo_arquivos)
#         self.arquivos.setRootIndex(self.modelo_arquivos.index(os.path.expanduser("~/Documentos/GitHub")))
#         self.arquivos.setMaximumHeight(200)  # Ajustando a altura
        
#         left_column.addWidget(self.arquivos)

#         # Seção 2: Configurações
#         self.configuracoes = QTabWidget()
#         self.configuracoes.addTab(QWidget(), "Layout")
#         self.janelas_tab = QWidget()
#         self.configuracoes.addTab(self.janelas_tab, "Janelas")
#         self.configuracoes.setMaximumHeight(150)  # Ajustando a altura
#         left_column.addWidget(self.configuracoes)

#         layout.addLayout(left_column, 0, 0, 3, 1)

#         # Espaço entre as colunas
#         layout.setColumnMinimumWidth(1, 20)

#         # Coluna da direita
#         right_column = QVBoxLayout()

#         # Seção 4: Visualização
#         self.visualizacao = QLabel("Visualização")
#         self.visualizacao.setStyleSheet("background-color: #444; color: white; text-align: center;")
#         self.visualizacao.setFixedSize(200, 200)  # Definindo como um quadrado
#         right_column.addWidget(self.visualizacao)

#         # Espaço entre visualização e diagnóstico
#         right_column.addSpacing(20)

#         # Seção 3: Diagnóstico
#         self.diagnostico = QPlainTextEdit()
#         self.diagnostico.setPlaceholderText("Logs e notificações...")
#         self.diagnostico.setReadOnly(True)
#         self.diagnostico.setFixedHeight(200)  # Ajustando a altura do diagnóstico
#         right_column.addWidget(self.diagnostico)

#         layout.addLayout(right_column, 0, 2, 3, 1)

#         # Criando lista para armazenar janelas abertas
#         self.janelas_abertas = []

#         # Botão para abrir nova janela
#         janelas_layout = QVBoxLayout()
#         self.janelas_tab.setLayout(janelas_layout)
#         self.nova_janela_btn = QPushButton("Criar Nova Janela")
#         self.nova_janela_btn.clicked.connect(self.criar_nova_janela)
#         janelas_layout.addWidget(self.nova_janela_btn)

#         # Estilos
#         self.setStyleSheet(
#             "QTreeView { background-color: #222; color: white; padding: 5px; }"
#             "QTextEdit { background-color: #111; color: #0f0; font-family: monospace; }"
#             "QPlainTextEdit { background-color: #000; color: #0f0; font-family: monospace; }"
#             "QLabel { background-color: #444; color: white; text-align: center; }"
#             "QWidget { background-color: #333; }"
#             "QPushButton { background-color: #555; color: white; padding: 5px; border-radius: 5px; }"
#             "QGroupBox { background-color: #222; color: white; border: 1px solid gray; padding: 5px; }"
#         )

#     def criar_nova_janela(self):
#         nova_janela = AssistenteUI()
#         self.janelas_abertas.append(nova_janela)  # Mantém a referência para evitar que seja destruída
#         nova_janela.show()

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     janela = AssistenteUI()
#     janela.show()
#     sys.exit(app.exec())

# from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QPlainTextEdit, QTabWidget
# import sys

# class NovaJanela(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Painel Secundário")
#         self.setGeometry(200, 200, 600, 400)

#         layout = QVBoxLayout()
#         central_widget = QWidget()
#         central_widget.setLayout(layout)
#         self.setCentralWidget(central_widget)

#         # Adicionando widgets diferentes
#         self.label = QLabel("📊 Painel de Controle Avançado")
#         self.label.setStyleSheet("color: cyan; font-size: 18px; font-weight: bold;")

#         self.log_area = QPlainTextEdit()
#         self.log_area.setPlaceholderText("Área de Logs e Monitoramento...")
#         self.log_area.setStyleSheet("background-color: #222; color: lime; font-family: monospace;")

#         self.botao_atualizar = QPushButton("Atualizar Dados")
#         self.botao_atualizar.clicked.connect(self.atualizar_logs)

#         layout.addWidget(self.label)
#         layout.addWidget(self.log_area)
#         layout.addWidget(self.botao_atualizar)

#     def atualizar_logs(self):
#         self.log_area.appendPlainText("🔄 Dados atualizados com sucesso!")

# class AssistenteUI(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Assistente Futurista")
#         self.setGeometry(100, 100, 1200, 800)

#         # Criando layout principal
#         central_widget = QWidget()
#         self.setCentralWidget(central_widget)
#         layout = QVBoxLayout()
#         central_widget.setLayout(layout)

#         self.configuracoes = QTabWidget()
#         self.configuracoes.addTab(QWidget(), "Configuração")
#         self.janelas_tab = QWidget()
#         self.configuracoes.addTab(self.janelas_tab, "Janelas")

#         layout.addWidget(self.configuracoes)

#         # Botão para abrir nova janela personalizada
#         janelas_layout = QVBoxLayout()
#         self.janelas_tab.setLayout(janelas_layout)
#         self.nova_janela_btn = QPushButton("Abrir Painel Secundário")
#         self.nova_janela_btn.clicked.connect(self.abrir_painel_secundario)
#         janelas_layout.addWidget(self.nova_janela_btn)

#         # Lista para armazenar janelas abertas
#         self.janelas_abertas = []

#     def abrir_painel_secundario(self):
#         nova_janela = NovaJanela()
#         self.janelas_abertas.append(nova_janela)
#         nova_janela.show()

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     janela = AssistenteUI()
#     janela.show()
#     sys.exit(app.exec())


# import sys
# import psutil
# from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QProgressBar, QHBoxLayout, QPushButton, QFrame

# class TelaDiagnostico(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Monitoramento do Sistema")
#         self.setGeometry(150, 150, 800, 600)

#         # Layout principal
#         layout = QVBoxLayout()
#         central_widget = QWidget()
#         central_widget.setLayout(layout)
#         self.setCentralWidget(central_widget)

#         # Título
#         self.label_titulo = QLabel("📊 Monitor do Sistema")
#         self.label_titulo.setStyleSheet("font-size: 22px; font-weight: bold; color: cyan;")
#         layout.addWidget(self.label_titulo)

#         # Layout para os monitores de CPU, RAM e Disco
#         monitor_layout = QVBoxLayout()

#         self.cpu_label = QLabel("CPU:")
#         self.cpu_bar = QProgressBar()
#         self.ram_label = QLabel("RAM:")
#         self.ram_bar = QProgressBar()
#         self.disk_label = QLabel("Disco:")
#         self.disk_bar = QProgressBar()

#         # Adicionando ao layout
#         monitor_layout.addWidget(self.cpu_label)
#         monitor_layout.addWidget(self.cpu_bar)
#         monitor_layout.addWidget(self.ram_label)
#         monitor_layout.addWidget(self.ram_bar)
#         monitor_layout.addWidget(self.disk_label)
#         monitor_layout.addWidget(self.disk_bar)

#         layout.addLayout(monitor_layout)

#         # Caixa personalizável
#         self.custom_box = QFrame()
#         self.custom_box.setStyleSheet("background-color: #222; border: 1px solid cyan;")
#         self.custom_box.setFixedHeight(200)
#         layout.addWidget(self.custom_box)

#         # Botão para atualizar diagnóstico
#         self.btn_atualizar = QPushButton("Atualizar Diagnóstico")
#         self.btn_atualizar.clicked.connect(self.atualizar_diagnostico)
#         layout.addWidget(self.btn_atualizar)

#         # Atualizar diagnóstico na inicialização
#         self.atualizar_diagnostico()

#     def atualizar_diagnostico(self):
#         self.cpu_bar.setValue(int(psutil.cpu_percent()))
#         self.ram_bar.setValue(int(psutil.virtual_memory().percent))
#         self.disk_bar.setValue(int(psutil.disk_usage('/').percent))


# class AssistenteUI(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Assistente Futurista")
#         self.setGeometry(100, 100, 1200, 800)

#         # Layout principal
#         central_widget = QWidget()
#         self.setCentralWidget(central_widget)
#         layout = QVBoxLayout()
#         central_widget.setLayout(layout)

#         # Botão para abrir monitoramento do sistema
#         self.btn_monitoramento = QPushButton("Abrir Monitoramento do Sistema")
#         self.btn_monitoramento.clicked.connect(self.abrir_monitoramento)
#         layout.addWidget(self.btn_monitoramento)

#         # Lista de janelas abertas
#         self.janelas_abertas = []

#     def abrir_monitoramento(self):
#         nova_tela = TelaDiagnostico()
#         self.janelas_abertas.append(nova_tela)
#         nova_tela.show()

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     janela = AssistenteUI()
#     janela.show()
#     sys.exit(app.exec())
