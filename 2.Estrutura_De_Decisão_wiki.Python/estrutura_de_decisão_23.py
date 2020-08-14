#  Faça um Programa que peça um número e informe se o número é inteiro ou decimal.
#  Dica: utilize uma função de arredondamento.

numero = float(input('Insira um número: '))
checar_numero = round(numero)

if numero == checar_numero:
    print(f'Esse número é um inteiro: {numero}')
elif numero != checar_numero:
    print(f'Esse número é um decimal: {numero}')
