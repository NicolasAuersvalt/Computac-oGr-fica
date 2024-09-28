from header import *  # Certifique-se de que o arquivo header.py contém os imports necessários

# Função para criar um gráfico 3D do cubo
def plot_matriz_3d(matriz):
    arestas = [
        [0, 1], [1, 2], [2, 3], [3, 0],  # Base
        [4, 5], [5, 6], [6, 7], [7, 4],  # Topo
        [0, 4], [1, 5], [2, 6], [3, 7]   # Conexões
    ]
    
    x = matriz[:, 0]
    y = matriz[:, 1]
    z = matriz[:, 2]

    fig = go.Figure()

    for aresta in arestas:
        fig.add_trace(go.Scatter3d(
            x=[x[aresta[0]], x[aresta[1]]],
            y=[y[aresta[0]], y[aresta[1]]],
            z=[z[aresta[0]], z[aresta[1]]],
            mode='lines',
            line=dict(color='blue', width=5)
        ))

    # Definir os limites dos eixos manualmente para 10x10x10
    fig.update_layout(title="Visualização 3D do Cubo", autosize=True,
                      scene=dict(
                          xaxis=dict(range=[-5, 5]),
                          yaxis=dict(range=[-5, 5]),
                          zaxis=dict(range=[-5, 5])
                      ),
                      margin=dict(l=65, r=50, b=65, t=90))
    return fig

# Função para multiplicar matrizes
def multiplicar_matrizes(matriz1, matriz2):
    return np.dot(matriz1, matriz2)

# Título da Aplicação
st.title("Operações com Matrizes com Visualização 3D")

# Menu lateral para escolher a operação
st.sidebar.title("Menu")
opcao = st.sidebar.selectbox("Escolha a operação", ("Ampliação", "Translação", "Rotação"))

# Entrada de texto para a matriz inicial
matriz_str = st.text_area("Matriz (use notação Python, ex: [[0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0], [0, 0, 1], [1, 0, 1], [1, 1, 1], [0, 1, 1]])", 
                          "[[0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0], [0, 0, 1], [1, 0, 1], [1, 1, 1], [0, 1, 1]]")

# Converter a string de entrada para lista
matriz = np.array(eval(matriz_str))

# Verificar se a matriz é 3xn
if matriz.shape[1] != 3:
    st.error("A matriz deve ter 3 colunas.")
else:
    if opcao == "Ampliação":
        coef = st.number_input("Coeficiente de Ampliação:", value=1.0, min_value=0.0)
        # Multiplicando a matriz pelos coeficientes de ampliação
        resultado = matriz * coef

    elif opcao == "Translação":
        # Sliders para descolamento
        deslocamento_x = st.slider("Deslocamento X", min_value=-10.0, max_value=10.0, value=0.0)
        deslocamento_y = st.slider("Deslocamento Y", min_value=-10.0, max_value=10.0, value=0.0)
        deslocamento_z = st.slider("Deslocamento Z", min_value=-10.0, max_value=10.0, value=0.0)

        # Criar a matriz de deslocamento
        matriz_deslocamento = np.array([
            [deslocamento_x] * matriz.shape[0],
            [deslocamento_y] * matriz.shape[0],
            [deslocamento_z] * matriz.shape[0]
        ]).T

        # Somar as matrizes
        resultado = matriz + matriz_deslocamento

    elif opcao == "Rotação":
        angulo = st.slider("Ângulo de Rotação (graus)", min_value=0, max_value=360, value=45)
        eixo = st.selectbox("Escolha o eixo de rotação", ("X", "Y", "Z"))
        angulo_rad = np.radians(angulo)

        if eixo == "X":
            matriz_rotacao = np.array([[1, 0, 0],
                                        [0, np.cos(angulo_rad), -np.sin(angulo_rad)],
                                        [0, np.sin(angulo_rad), np.cos(angulo_rad)]])
        elif eixo == "Y":
            matriz_rotacao = np.array([[np.cos(angulo_rad), 0, np.sin(angulo_rad)],
                                        [0, 1, 0],
                                        [-np.sin(angulo_rad), 0, np.cos(angulo_rad)]])
        else:  # Z
            matriz_rotacao = np.array([[np.cos(angulo_rad), -np.sin(angulo_rad), 0],
                                        [np.sin(angulo_rad), np.cos(angulo_rad), 0],
                                        [0, 0, 1]])

        resultado = multiplicar_matrizes(matriz_rotacao, matriz.T).T

    if resultado is not None:

        # Plotar o gráfico 3D do resultado
        st.plotly_chart(plot_matriz_3d(resultado))

        # Exibir o resultado
        st.write("Resultado:")
        st.write(resultado)
