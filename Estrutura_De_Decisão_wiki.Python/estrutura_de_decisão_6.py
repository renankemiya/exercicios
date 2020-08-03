#  Faça um Programa que leia três números e mostre o maior deles.

numero_1 = float(input('Insira o primeiro número: '))
numero_2 = float(input('Insira o segundo número: '))
numero_3 = float(input('Insira o terceiro número: '))

if numero_1 > numero_2:
    if numero_1 > numero_3:
        print(f'O primeiro é o maior: {numero_1}')
    elif numero_1 < numero_3:
        print(f'O terceiro é o maior: {numero_3}')
    else:
        print(f'O primeiro e o terceiro são iguais: {numero_1}, {numero_3}')
elif numero_2 > numero_3:
    if numero_2 > numero_1:
        print(f'O segundo é o maior: {numero_2}')
    elif numero_2 < numero_1:
        print(f'O primeiro é o maior: {numero_1}')
    else:
        print(f'O segundo e o primeiro são iguais: {numero_2}, {numero_1}')
elif numero_3 > numero_1:
    if numero_3 > numero_2:
        print(f'O terceiro é o maior: {numero_3}')
    elif numero_3 < numero_2:
        print(f'O segundo é o maior: {numero_2}')
    else:
        print(f'O terceiro e o segundo são iguais: {numero_3}, {numero_2}')
else:
    print(f'Todos os números são iguais: {numero_1}, {numero_2}, {numero_3}')

#  Correção da internet

number1 = input("digite um numero ---> ")
number2 = input("digite um numero ---> ")
number3 = input("digite um numero ---> ")
if (number1 > number2) and (number1 > number3):
    print(number1, "eh o maior numero")
if (number2 > number1) and (number2 > number3):
    print(number2, "eh o maior numero")
if (number3 > number1) and (number3 > number2):
    print(number3, "eh o maior numero")
