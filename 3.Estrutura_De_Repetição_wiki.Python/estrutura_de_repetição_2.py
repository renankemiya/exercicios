#  Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
#  mostrando uma mensagem de erro e voltando a pedir as informações.

nome = input('Digite seu usuário: ')
senha = input('Digite sua senha: ')

while nome == senha:
    print('O nome e a senha não podem ser iguais, tente novamente')
    nome = input('Digite seu usuário: ')
    senha = input('Digite sua senha: ')

if nome != senha:
    print('Usuário:', nome)
    print('Senha:', senha)
