# Dicionário de conversão para metros
fatores = {
    'km': 1000,
    'hm': 100,
    'dam': 10,
    'm': 1,
    'dm': 0.1,
    'cm': 0.01,
    'mm': 0.001
}

while True:
    # Entrada de valores
    valores = input().split(" ")
    
    # Separação das informações
    X = int(valores[0])
    unidade_X = valores[1]
    Y = int(valores[2])
    unidade_Y = valores[3]

    # Verifica condição de parada
    if X == 0 and Y == 0:
        break

    print(fatores[unidade_X]) #pega o valor associado a essa chave
    # Conversão para metros
    X_metros = X * fatores[unidade_X]
    Y_metros = Y * fatores[unidade_Y]
    
    # Soma em metros
    resultado = X_metros + Y_metros
    
    print(f"{resultado:.2f} m")

# # Unidade de medida    

# A principal unidade de comprimento é o metro. Entretanto, existem 
# situações em que essa unidade deixa de ser prática. Por exemplo, 
# se queremos medir a distância entre João Pessoa e Campina Grande, 
# a unidade metro é muito pequena. Por outro lado, se queremos medir 
# o comprimento de uma formiga, a unidade metro é muito grande. Nesses 
# casos, para facilitar, utilizamos os múltiplos e submúltiplos das 
# unidades de medidas. Os múltiplos e submúltiplos do metro, no
# Sistema Internacional de Medidas (SI), são apresentados na tabela 
# a seguir:

# <table>
# <tbody>
#     <tr>
#         <th>Fator</th>
#         <th>Símbolo</th>
#         <th>Nome</th>
#     </tr>
#     <tr>
#         <td>1000</td>
#         <td>km</td>
#         <td>quilômetro</td>
#     </tr>
#     <tr>
#         <td>100</td>
#         <td>hm</td>
#         <td>hectômetro</td>
#     </tr>
#     <tr>
#         <td>10</td>
#         <td>dam</td>
#         <td>decâmetro</td>
#     </tr>
#      <tr>
#          <td>1</td>
#          <td>m</td>
#          <td>metro</td>
#     </tr>
#     <tr>
#         <td>0,1</td>
#         <td>dm</td>
#         <td>decímetro</td>
#     </tr>
#     <tr>
#         <td>0,01</td>
#         <td>cm</td>
#         <td>centímetro</td>
#     </tr>
#     <tr>
#         <td>0,001</td>
#         <td>mm</td>
#         <td>milímetro</td>
#     </tr>
# </tbody>    
# </table>

# Um cientista precisa fazer várias medições e somá-las duas a duas. 
# Para ajudá-lo, você precisa desenvolver um programa que realize 
# essa soma para o cientista. O seu programa deve usar os símbolos 
# da tabela acima para realizar a soma de um conjunto de pares de 
# valores medidos pelo cientista. O resultado da
# soma deve ser impresso na unidade de medida básica (o metro).

# Dica: Use dicionário.

# ### Entrada

# Cada linha da entrada corresponde a um caso de teste diferente. 
# Cada caso de teste é composto por quatro informações: um inteiro 
# X e sua unidade de medida e mais um inteiro Y e sua unidade de 
# medida, todos separados por um espaço em branco.

# ### Saída

# Para cada caso de teste da entrada o seu programa deve imprimir 
# um número real Z que indique a soma X + Y juntamente com sua 
# unidade de medida. O resultado de cada soma deve possuir duas 
# casas decimas e estar na unidade de medida básica.O programa deve 
# parar quando ambos os valores a somar forem
# iguais a zero.

# # Exemplo

# ```
# $ python unidade.py
# 20 cm 1 m
# 2 km 80 cm
# 0 cm 0 m
# 1.20 m
# 2000.80 m
# ```
