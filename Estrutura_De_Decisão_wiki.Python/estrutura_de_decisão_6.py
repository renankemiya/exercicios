numero_1 = float(input('Insira o primeiro número: '))
numero_2 = float(input('Insira o segundo número: '))
numero_3 = float(input('Insira o terceiro número: '))

if numero_1 > numero_2 > numero_3:
    print(f'O primeiro número é {numero_1}')
elif numero_1 > numero_2 < numero_3:
    print(f'O primeiro número é {numero_1}')
elif numero_2 > numero_3 > numero_1:
    print(f'O segundo número é {numero_2}')
elif numero_2 > numero_3 < numero_1:
    print(f'O segundo número é {numero_2}')
elif numero_3 > numero_1 > numero_2:
    print(f'O terceiro número é {numero_3}')
elif numero_3 > numero_1 < numero_2:
    print(f'O terceiro número é {numero_3}')
else:
    print('Existem números iguais')
