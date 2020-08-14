#  Faça um Programa que verifique se uma letra digitada é "F" ou "M".
#  Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

sexo = input('Insira F ou M para informar seu genero: ')

if sexo == 'F':
    print('Feminino')
elif sexo == 'M':
    print('Masculino')
else:
    print('Sexo inválido')

#  Correção da internet

sexo = input("digite seu sexo \"F\" ou \"M\": ")
if sexo == "F" or sexo == "M":
    if sexo == "F":
        print("F - Feminino")
    else:
        print("M - Masculino")
else:
    print("sexo invalido")
