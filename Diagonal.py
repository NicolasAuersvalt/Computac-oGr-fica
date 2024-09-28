def diagonal(coeficientes):
    """
    Cria uma matriz diagonal com os coeficientes na diagonal principal

    """

    # Crio a matriz vazia
    tam = coeficientes.size()

    # Cria uma matriz de .zeros do tamanho tam x tam
    mat = np.zeros((tam,tam))


    # Cria uma matriz quadrada
    for i in size(tam):
        
        # Não preciso de mais um for pois vou colocar
        # os coeficientes em mat[i][i], que é a diagonal
        matriz[i][i] = coeficientes[i]
            

    return  matriz
