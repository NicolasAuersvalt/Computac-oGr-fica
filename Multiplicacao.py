# Multiplicacao.py
import numpy as np

def multiplicar_matrizes(matriz1, matriz2):
    """
    Multiplica duas matrizes usando NumPy.
    :param matriz1: Primeira matriz.
    :param matriz2: Segunda matriz.
    :return: Produto das duas matrizes.
    """
    return np.dot(matriz1, matriz2)
