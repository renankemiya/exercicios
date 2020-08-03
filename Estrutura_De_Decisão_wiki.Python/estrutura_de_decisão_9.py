#  Faça um Programa que leia três números e mostre-os em ordem decrescente.

numero_1 = float(input('Insira o primeiro número: '))
numero_2 = float(input('Insira o segundo número: '))
numero_3 = float(input('Insira o terceiro número: '))

if numero_1 > numero_2 > numero_3:
    print('Ordem: 1º, 2º, 3º: ', numero_1, numero_2, numero_3)
elif numero_1 > numero_3 > numero_2:
    print('Ordem: 1º, 3º, 2º: ', numero_1, numero_3, numero_2)
elif numero_2 > numero_1 > numero_3:
    print('Ordem: 2º, 1º, 3º: ', numero_2, numero_1, numero_3)
elif numero_2 > numero_3 > numero_1:
    print('Ordem: 2º, 3º, 1º: ', numero_2, numero_3, numero_1)
elif numero_3 > numero_1 > numero_2:
    print('Ordem: 3º, 1º, 2º: ', numero_3, numero_1, numero_2)
elif numero_3 > numero_2 > numero_1:
    print('Ordem: 3º, 2º, 1º: ', numero_3, numero_2, numero_1)
elif numero_1 == numero_2 > numero_3:
    print('Ordem: 1º e 2º iguais, 3º: ', numero_1, numero_2, numero_3)
elif numero_1 == numero_3 > numero_2:
    print('Ordem: 1º e 3º iguais, 2º: ', numero_1, numero_3, numero_2)
elif numero_2 == numero_3 > numero_1:
    print('Ordem: 2º e 3º iguais, 1º: ', numero_2, numero_3, numero_1)
else:
    print('Ordem: 1º, 2º e 3º são iguais: ', numero_1, numero_2, numero_3)

# Correção da internet

number1 = input("digite um numero ---> ")
number2 = input("digite um numero ---> ")
number3 = input("digite um numero ---> ")
if (number1 > number2) and (number1 > number3) and (number2 > number3):
    print(number1, " ", number2, " ", number3)
if (number1 > number2) and (number1 > number3) and (number3 > number2):
    print(number1, " ", number3, " ", number2)
if (number2 > number1) and (number2 > number3) and (number1 > number3):
    print(number2, " ", number1, " ", number3)
if (number2 > number1) and (number2 > number3) and (number3 > number1):
    print(number2, " ", number3, " ", number1)
if (number3 > number1) and (number3 > number2) and (number1 > number2):
    print(number3, " ", number1, " ", number2)
if (number3 > number1) and (number3 > number2) and (number2 > number1):
    print(number3, " ", number2, " ", number1)
