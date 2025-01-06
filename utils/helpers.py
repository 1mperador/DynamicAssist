import os
import cv2

def criar_diretorio(diretorio):
    """Cria um diretório se ele não existir."""
    if not os.path.exists(diretorio):
        os.makedirs(diretorio)

def salvar_imagem(caminho, imagem):
    """Salva uma imagem no caminho especificado."""
    cv2.imwrite(caminho, imagem)
