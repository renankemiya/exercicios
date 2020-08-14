#  Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

valor = float(input('Insira um número: '))

if valor > 0:
    print('O número tem valor positivo')
elif valor < 0:
    print('O número tem valor negativo')
else:
    print('O valor é 0')

# Correção da internet

number1 = float(input("digite um numero: "))
if number1 > 0:
    print(" é positivo ", number1)
if number1 < 0:
    print(" é negativo ", number1)
else:
    print(" é ZERO ", number1)
