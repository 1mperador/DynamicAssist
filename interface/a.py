
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


# # ---------------------------------------------------------------------------------------------

# class PainelFlutuante(QWidget):
#     def __init__(self, titulo, cor_inicial):
#         super().__init__()
#         self.setWindowTitle(titulo)
#         self.setGeometry(100, 100, 250, 150)
#         self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)

#         self.setAutoFillBackground(True)
#         self.atualizar_cor(cor_inicial)

#         self.label = QLabel(titulo, self)
#         self.label.setAlignment(Qt.AlignCenter)
#         self.label.setStyleSheet("color: white; font-size: 18px;")
#         self.label.setGeometry(0, 40, 250, 50)

#         self.animacao = QPropertyAnimation(self, b"geometry")

#     def atualizar_cor(self, cor):
#         palette = self.palette()
#         palette.setColor(QPalette.Window, cor)
#         self.setPalette(palette)

#     def mover_para(self, x, y):
#         atual = self.geometry()
#         novo = QRect(x, y, atual.width(), atual.height())
#         self.animacao.stop()
#         self.animacao.setDuration(500)
#         self.animacao.setStartValue(atual)
#         self.animacao.setEndValue(novo)
#         self.animacao.start()

#     def paintEvent(self, event):
#         super().paintEvent(event)
#         painter = QPainter(self)
#         pen = QPen(QColor("#9b59b6"))  # Roxo neon
#         pen.setWidth(4)
#         painter.setPen(pen)
#         painter.drawRect(0, 0, self.width() - 1, self.height() - 1)

from painel_base import PainelBase

class TerminalPainel(PainelBase):
    def __init__(self, x=0, y=0, w=400, h=300):
        super().__init__(x, y, w, h)