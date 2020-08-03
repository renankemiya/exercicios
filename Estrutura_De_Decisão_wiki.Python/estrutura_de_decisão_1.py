#  Faça um Programa que peça dois números e imprima o maior deles.

numero_1 = float(input('Insira um número: '))
numero_2 = float(input('Insira outro número: '))

if numero_1 > numero_2:
    print(f'O primeiro número é maior: {numero_1}')
elif numero_2 > numero_1:
    print(f'O segundo número é maior: {numero_2}')
else:
    print(f'Os números são iguais: {numero_1}')

#  Correção da internet

number1 = input("digite um numero: ")
number2 = input("digite outro numero: ")

if number1 > number2:
    print("o maior numero eh ---> ", number1)
if number2 > number1:
    print("o maior numero eh ---> ", number2)
else:
    print(number1, " = ", number2)
