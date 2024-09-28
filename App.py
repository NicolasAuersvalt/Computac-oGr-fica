from header import *  # Certifique-se de que o arquivo header.py contém os imports necessários

# Função para a página inicial
import streamlit as st

def pagina_inicial():
    st.title("Bem-vindo ao Aplicativo de Computação Gráfica!")

    # Exibir uma imagem a partir de um arquivo local
    imagem_path = "imagem/coordenada.PNG"  # Substitua pelo caminho da sua imagem

    st.write("""
        Este aplicativo é uma aplicação da Álgebra Linear na computação gráfica.
        
        As operações disponíveis incluem:
        - **Ampliação:** Altera o tamanho da matriz.
            - Primeiro, toma-se uma Matriz de Pontos Iniciais (MPI) de dimensão 3 x N, com todos os pontos da figura;
            - Segundo, recebe-se o valor do Coeficiente de Ampliação (CA);
            - Terceiro, cria-se uma Matriz de Transformação Linear (MTL), que é uma matriz diagonal preenchida com CA;
            - Quarto, cria-se uma Matriz de Pontos Finais (MPF) de dimensão 3 x N, inicialmente zerada;
            - Quinto, realiza-se a operação MPF = MTL * MPI (multiplicação, não adição);
            - Sexto, MPF é uma matriz de dimensão 3 x N, então para cada coluna, plota-se um vértice;
            - **OBS:** 3 x N porque devem haver 3 linhas (x, y, z), e N porque podem existir vários pontos. Além disso, deve-se ter como referência quais são os pontos ligantes.

        - **Translação:** Move a matriz em uma direção especificada.
            - Primeiro, toma-se uma Matriz de Pontos Iniciais (MPI) de dimensão 3 x N, com todos os pontos da figura;
            - Segundo, recebe-se uma Matriz de Translação (MT), que deve ter dimensões 3 x N;
            - Terceiro, cria-se uma Matriz de Pontos Finais (MPF) de dimensão 3 x N, inicialmente zerada;
            - Quarto, realiza-se a operação MPF = MPI + MT (adição);
            - Quinto, MPF é uma matriz de dimensão 3 x N, então para cada coluna, plota-se um vértice;
            - **OBS:** MT pode ser um vetor (x, y, z), então é prolongado para uma matriz 3 x N, com todas as colunas sendo (x, y, z).

        - **Rotação:** Rotaciona a matriz em torno dos eixos X, Y ou Z.
            - Primeiro, toma-se uma Matriz de Pontos Iniciais (MPI) de dimensão 3 x N, com todos os pontos da figura;
            - Segundo, recebe-se os ângulos de rotação (a, b, c) em relação aos eixos X, Y e Z;
            - Terceiro, cria-se uma Matriz de Pontos Finais (MPF) de dimensão 3 x N, inicialmente zerada;
            - Quarto, cria-se Matrizes de Rotação (MR) para cada rotação (MRx, MRy ou MRz);
            - Quinto, realiza-se a conversão das coordenadas x, y e z de acordo com as matrizes de rotação.
    """)

    st.image(imagem_path, caption="Conversão para Polar", width=400)

    st.write("""
        - **Sexto:** Para uma rotação em Z, a matriz ficaria [[cos(a), -sen(a), 0], [sen(a), cos(a), 0], [0, 0, 1]];
        - **Sétimo:** Realiza-se a operação MR = MRx * MRy * MRz (multiplicação das matrizes de rotação);
        - **Oitavo:** MR é uma matriz de dimensão 3 x N, então para cada coluna, plota-se um vértice.
    """)


# Função para as operações
def pagina_operacoes():
    st.title("Operações com Matrizes com Visualização 3D")

    # Menu lateral para escolher a operação
    opcao = st.sidebar.selectbox("Escolha a operação", ("Ampliação", "Translação", "Rotação"))

    # Entrada de texto para a matriz inicial
    matriz_str = st.text_area("Matriz do CUBO (use notação Python, ex: [[0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0], [0, 0, 1], [1, 0, 1], [1, 1, 1], [0, 1, 1]])", 
                              "[[0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0], [0, 0, 1], [1, 0, 1], [1, 1, 1], [0, 1, 1]]")

    # Converter a string de entrada para lista
    try:
        matriz = np.array(eval(matriz_str))
    except Exception as e:
        st.error("Erro ao converter a matriz. Verifique a entrada.")

    # Verificar se a matriz é 3xn
    if matriz.ndim != 2 or matriz.shape[1] != 3:
        st.error("A matriz deve ter 3 colunas.")
    else:
        resultado = None

        if opcao == "Ampliação":
            resultado = ampliar(matriz)

        elif opcao == "Translação":
            resultado = transladar(matriz)

        elif opcao == "Rotação":
            resultado = rotacionar(matriz)

        if resultado is not None:
            # Plotar o gráfico 3D do resultado
            st.plotly_chart(plot_matriz_3d(resultado))

            # Exibir o resultado
            st.write("Resultado:")
            st.write(resultado)

# Seleção de página no menu lateral
pagina = st.sidebar.selectbox("Escolha a página", ("Página Inicial", "Operações"))

if pagina == "Página Inicial":
    pagina_inicial()
else:
    pagina_operacoes()
