import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QTextEdit, QPushButton
from PyQt5.QtCore import Qt, QPropertyAnimation, QRect, QTimer, QProcess
from PyQt5.QtGui import QPalette, QColor, QPainter, QPen

class PainelFlutuante(QWidget):
    def __init__(self, titulo, cor_inicial):
        super().__init__()
        self.setWindowTitle(titulo)
        self.setGeometry(100, 100, 250, 150)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)

        self.setAutoFillBackground(True)
        self.atualizar_cor(cor_inicial)

        self.label = QLabel(titulo, self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("color: white; font-size: 18px;")
        self.label.setGeometry(0, 40, 250, 50)

        self.animacao = QPropertyAnimation(self, b"geometry")

    def atualizar_cor(self, cor):
        palette = self.palette()
        palette.setColor(QPalette.Window, cor)
        self.setPalette(palette)

    def mover_para(self, x, y):
        atual = self.geometry()
        novo = QRect(x, y, atual.width(), atual.height())
        self.animacao.stop()
        self.animacao.setDuration(500)
        self.animacao.setStartValue(atual)
        self.animacao.setEndValue(novo)
        self.animacao.start()

    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter(self)
        pen = QPen(QColor("#9b59b6"))  # Roxo neon
        pen.setWidth(2)  # Linha mais fina para o terminal
        painter.setPen(pen)
        painter.drawRect(0, 0, self.width() - 1, self.height() - 1)

class PainelBtop(PainelFlutuante):
    def __init__(self, titulo, cor_inicial):
        super().__init__(titulo, cor_inicial)

        layout = QVBoxLayout(self)

        self.output = QTextEdit()
        self.output.setReadOnly(True)
        self.output.setStyleSheet("background-color: #000; color: #0f0; font-family: monospace; font-size: 12px;")

        layout.addWidget(self.output)
        self.setLayout(layout)

        # Processo que executa o btop
        self.processo = QProcess(self)
        self.processo.setProcessChannelMode(QProcess.MergedChannels)  # Junta stdout e stderr
        self.processo.readyReadStandardOutput.connect(self.ler_saida)

        self.processo.start("btop")  # Assumindo que btop está instalado no sistema

    def ler_saida(self):
        saida = bytes(self.processo.readAllStandardOutput()).decode("utf-8", errors="ignore")
        self.output.setPlainText(saida)  # Sobrescreve tudo (pois btop redesenha sempre)
        self.output.verticalScrollBar().setValue(0)  # Mantém no topo


class PainelTerminal(PainelFlutuante):
    def __init__(self, titulo, cor_inicial):
        super().__init__(titulo, cor_inicial)

        layout = QVBoxLayout(self)

        self.output = QTextEdit()
        self.output.setReadOnly(True)
        self.output.setStyleSheet("background-color: #000; color: #0f0; font-family: monospace;")

        self.input = QTextEdit()
        self.input.setFixedHeight(40)
        self.input.setStyleSheet("background-color: #111; color: #fff; font-family: monospace;")

        self.botao_enviar = QPushButton("Enviar")
        self.botao_enviar.setStyleSheet("background-color: #9b59b6; color: white;")

        layout.addWidget(self.output)
        layout.addWidget(self.input)
        layout.addWidget(self.botao_enviar)

        self.setLayout(layout)

        # Processo que executa test.py
        self.processo = QProcess(self)
        self.processo.readyReadStandardOutput.connect(self.ler_saida)
        self.processo.readyReadStandardError.connect(self.ler_erro)

        self.processo.start("python3", ["test.py"])  # ou "python" se for Windows

        self.botao_enviar.clicked.connect(self.enviar_comando)

    def ler_saida(self):
        saida = bytes(self.processo.readAllStandardOutput()).decode("utf-8")
        self.output.append(saida)

    def ler_erro(self):
        erro = bytes(self.processo.readAllStandardError()).decode("utf-8")
        self.output.append(f"<span style='color:red'>{erro}</span>")

    def enviar_comando(self):
        comando = self.input.toPlainText().strip()
        if comando:
            self.processo.write((comando + "\n").encode())
            self.output.append(f"> {comando}")
            self.input.clear()

class MainApp(QApplication):
    def __init__(self, argv):
        super().__init__(argv)

        # Cria as janelas flutuantes
        self.painel1 = PainelFlutuante("Painel 1", QColor("#222"))
        self.painel2 = PainelFlutuante("Painel 2", QColor("#333"))
        self.painel3 = PainelFlutuante("Painel 3", QColor("#444"))

        self.painel1.show()
        self.painel2.show()
        self.painel3.show()

        # Posição inicial
        self.posicoes = [
            (100, 100),
            (400, 100),
            (700, 100)
        ]
        self.index = 0

        # Atualiza as posições a cada 8 segundos
        self.timer = QTimer()
        self.timer.timeout.connect(self.mover_paineis)
        self.timer.start(8000)
        self.mover_paineis()  # Primeira chamada

        # Aba fixa no canto inferior direito
        self.fixa = PainelTerminal("Terminal", QColor("#1e1e1e"))
        largura_tela = QApplication.primaryScreen().size().width()
        altura_tela = QApplication.primaryScreen().size().height()
        self.fixa.setGeometry(largura_tela - 620, altura_tela - 340, 600, 300)
        self.fixa.show()

        # Painel de diagnóstico com btop
        self.btop_painel = PainelBtop("Diagnóstico", QColor("#1c1c1c"))
        self.btop_painel.setGeometry(600, 100, 600, 400)
        self.btop_painel.show()


    def mover_paineis(self):
        for i, painel in enumerate([self.painel1, self.painel2, self.painel3]):
            nova_pos = self.posicoes[(self.index + i) % len(self.posicoes)]
            painel.mover_para(*nova_pos)
        self.index = (self.index + 1) % len(self.posicoes)

if __name__ == "__main__":
    app = MainApp(sys.argv)
    sys.exit(app.exec_())
