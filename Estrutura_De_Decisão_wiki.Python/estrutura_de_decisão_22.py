#  Faça um Programa que peça um número inteiro e determine se ele é par ou impar.
#  Dica: utilize o operador módulo (resto da divisão).

numero = int(input('Insira um número inteiro: '))
resto = numero % 2

if resto == 0:
    print(f'{numero} é um número par')
elif resto != 0:
    print(f'{numero} é um numero impar')
