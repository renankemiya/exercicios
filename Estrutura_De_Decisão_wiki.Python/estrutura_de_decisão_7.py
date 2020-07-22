numero_1 = float(input('Insira o primeiro número: '))
numero_2 = float(input('Insira o segundo número: '))
numero_3 = float(input('Insira o terceiro número: '))

if numero_1 > numero_2 > numero_3:
    print(f'O primeiro número é o maior, {numero_1}, e o terceiro é o menor, {numero_3}')
elif numero_1 > numero_2 < numero_3:
    print(f'O primeiro número é o maior, {numero_1}, e o segundo é o menor, {numero_2}')
elif numero_2 > numero_3 > numero_1:
    print(f'O segundo número é o maior, {numero_2}, e o primeiro é o menor, {numero_1}')
elif numero_2 > numero_3 < numero_1:
    print(f'O segundo número é o maior, {numero_2}, e o terceiro é o menor, {numero_3}')
elif numero_3 > numero_1 > numero_2:
    print(f'O terceiro número é o maior, {numero_3}, e o segundo é o menor, {numero_2}')
elif numero_3 > numero_1 < numero_2:
    print(f'O terceiro número é o maior, {numero_3}, e o segundo é o menor, {numero_1}')
else:
    print('Existem números iguais')
