import sounddevice as sd
import numpy as np

def detectar_audio(limiar=0.01, duracao=1):
    """
    Detecta som acima de um limite.
    :param limiar: Amplitude mínima para considerar som.
    :param duracao: Tempo (em segundos) para captura de som.
    :return: True se som for detectado, caso contrário False.
    """
    print("Analisando som...")
    audio = sd.rec(int(duracao * 44100), samplerate=44100, channels=1, dtype='float64')
    sd.wait()  # Aguarda a gravação terminar
    if np.max(np.abs(audio)) > limiar:
        return True
    return False
