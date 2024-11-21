def quantidade_usuarios(cadastro):
    contador = 0
    for chave, valor in cadastro.items():
        if chave != 9999:
            contador += len(valor) 
    return contador


lsd = {1234: ['Andrey'], 1226: ['Nazareno', 'Livia'], 9999: ['administrador']}
deq = {1114: ['Ana']}

assert quantidade_usuarios(lsd) == 3
assert quantidade_usuarios(deq) == 1


# # Quantidade de Usuários

# Uma empresa de segurança patrimonial mantém um registro de senhas e
# usuários. Em algumas situações, a mesma senha é compartilhada por 
# mais de um usuário. Pede-se que você implemente a função
# **quantidade_usuarios(cadastro)** que retorna a quantidade de 
# pessoas que tem senha de acesso. O parâmetro cadastro é um dicionário 
# em que as chaves são senhas e os valores são listas de nomes de 
# usuários que compartilham aquela senha. Vale ressaltar que a senha 
# 9999 é reservada para o 'administrador' do sistema. Ele pode aparecer 
# no cadastro, mas não deve ser contabilizado na
# quantidade de usuários que a função deve retornar.
