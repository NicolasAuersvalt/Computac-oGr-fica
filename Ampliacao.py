from header import *

def ampliar(matriz):

    coef = st.number_input("Coeficiente de Ampliação:", value=1.0, min_value=0.0)

    # Multiplicando a matriz pelos coeficientes de ampliação
    resultado = matriz * coef

    return resultado
