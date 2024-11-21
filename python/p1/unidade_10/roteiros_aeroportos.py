def eh_roteiro(iata, voos, roteiro):
    cidades = roteiro.split('/')  # Divide o roteiro em cidades
    for i in range(len(cidades) - 1):
        origem = iata[cidades[i]]  # Obtém o código IATA da cidade de origem
        destino = iata[cidades[i + 1]]  # Obtém o código IATA da cidade de destino
        
        # Verifica se há voos diretos de origem para destino
        tem_voo = False
        for aeroporto in voos[origem]:  # Itera pelos aeroportos de destino a partir da origem
            if aeroporto == destino:  # Compara se é igual ao destino
                tem_voo = True
                break  # Para a busca se encontrar

        if not tem_voo:  # Se não encontrou voo, retorna False
            return False
            
    return True  # Retorna True se todos os trechos têm voos diretos

# def eh_roteiro(iata, voos, roteiro):
#     # Passo 1: Dividir o roteiro em uma lista de cidades
#     cidades = roteiro.split("/")  # Exemplo: ['Campina Grande', 'Recife', 'Rio de Janeiro']
    
#     # Passo 2: Verificar se os voos são válidos
#     for i in range(len(cidades) - 1):  # Percorre até a penúltima cidade
#         origem = cidades[i]  # Cidade atual
#         destino = cidades[i + 1]  # Próxima cidade
        
#         # Verifica se a cidade existe no dicionário IATA
#         if origem not in iata or destino not in iata:
#             return False  # Se uma cidade não existe, o roteiro é inválido
        
#         codigo_origem = iata[origem]  # Obtém o código IATA da cidade atual
#         codigo_destino = iata[destino]  # Obtém o código IATA da próxima cidade
        
#         # Passo 3: Verifica se há um voo direto
#         if codigo_destino not in voos[codigo_origem]:
#             return False  # Se não há voo direto, o roteiro é inválido
            
#     return True  # Se todos os voos são válidos, retorna True

# Testes
iata = {
    "Campina Grande": "CPV",
    "Recife": "REC",
    "Salvador": "SSA",
    "Brasilia": "BSB",
    "Sao Paulo": "GRU",
    "Rio de Janeiro": "GIG"
}

voos = {
    "CPV": ["REC", "SSA"],
    "REC": ["CPV", "BSB", "GRU", "GIG"],
    "SSA": ["REC", "GRU", "GIG"],
    "BSB": ["CPV", "GIG", "GRU"],
    "GRU": ["GIG", "BSB"],
    "GIG": ["GRU", "REC"]
}

# Testando
print(eh_roteiro(iata, voos, "Campina Grande/Recife/Rio de Janeiro"))  # True
print(eh_roteiro(iata, voos, "Sao Paulo/Rio de Janeiro/Recife/Brasilia"))  # True
print(eh_roteiro(iata, voos, "Recife/Rio de Janeiro/Salvador/Recife"))  # False


# Roteiros Aeroportos

# Os aeroportos são identificados através de um código
# definido pela IATA (Associação Internacional de
# Transporte Aéreo). O código IATA é formado por 3 letras
# e designa unicamente um aeroporto. Por exemplo, o código
# IATA para o Aeroporto João Suassuna em Campina Grande é
# CPV, o Aeroporto Tom Jobim no Rio de Janeiro é GIG e o
# Aeroporto de Guarulhos em São Paulo é GRU.

# Uma outra informação importante vinculada a cada
# aeroporto é a indicação dos vôos diretos que tem origem
# no referido aeroporto. Por exemplo, os aeroportos que
# são contemplados com vôos diretos que partem de CPV
# (aeroporto de Campina Grande) são REC e SSA. Isso indica
# que é possível sair de CPV e chegar em REC, sem escalas.
# Da mesma forma, é possível sair  de CPV e chegar em SSA,
# sem escalas.

# Um roteiro de viagem aérea pode ser visto como uma
# composição de vôos diretos entre aeroportos. O roteiro
# Campina Grande/Recife/São Paulo/Brasília/Campina Grande
# indica que o vôo sai de campina Grande para Recife,
# depois de Recife para São Paulo, depois de São Paulo
# para Brasília e, finalmente, de Brasília para Campina
# Grande.

# Crie uma função que recebe dois mapas (um com o
# mapeamento do código IATA para os aeroportos e outro com
# as informações de vôos diretos de cada aeroporto) e um
# roteiro de viagem aérea. A função deve retornar True se
# o roteiro é possível de ser realizado e False, caso
# contrário. Vamos assumir que cada cidade tem apenas um
# aeroporto e que o roteiro de viagem contempla pelo menos
# duas cidades.
