def adiciona_sombra(img):
    for i in range(len(img)):
        for j in range(1, len(img[i])): 
            if img[i][j-1] <= 20:  # verifica o pixel à esquerda
                img[i][j] = img[i][j] // 2
    return img

# Teste
img = [[255, 255, 255, 255, 255, 255, 255],
       [255, 20, 20, 20, 20, 255, 255],
       [255, 20, 255, 255, 20, 255, 255],
       [255, 20, 255, 255, 20, 255, 255],
       [255, 20, 255, 255, 20, 255, 255],
       [255, 20, 20, 20, 20, 255, 255],
       [255, 255, 255, 255, 255, 255, 255],
       [255, 255, 255, 255, 255, 255, 255]]

adiciona_sombra(img)

assert img == [[255, 255, 255, 255, 255, 255, 255],
                [255, 20, 10, 10, 10, 127, 255],
                [255, 20, 127, 255, 20, 127, 255],
                [255, 20, 127, 255, 20, 127, 255],
                [255, 20, 127, 255, 20, 127, 255],
                [255, 20, 10, 10, 10, 127, 255],
                [255, 255, 255, 255, 255, 255, 255],
                [255, 255, 255, 255, 255, 255, 255]]


# # Sombra em pixels

# Em um aplicativo gráfico, imagens em preto e branco são
# representadas na forma de matrizes de valores inteiros
# correspondentes a um byte (entre 0 e 255). O valor 255
# representa branco e o valor 0 representa preto.

# Para simular a adição de uma sombra aos pixels que compõem a
# imagem, um dos desenvolvedores imaginou que bastaria escurecer
# suavemente os pixels brancos que sejam vizinhos de pixels
# escuros. Pede-se que você implemente uma função que faça
# exatamente isso.

# ## Especificação da função

# A função, de nome `adiciona_sombra(img)` recebe uma imagem na
# forma de uma matriz de inteiros (valores de 0 a 255). A
# função deve alterar todos os pixels que imediatamente à
# esquerda tenham um pixel muito escuro (valor menor ou igual
# 20). Para escurecer o pixel claro, o valor dele deve ser
# dividido por dois (divisão inteira).  

# <small> Atualizado por Jorge Figueiredo em 06/05/2024</small>
