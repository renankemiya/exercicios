numero_1 = float(input('Insira o primeiro número: '))
numero_2 = float(input('Insira o segundo número: '))
numero_3 = float(input('Insira o terceiro número: '))

if numero_1 > numero_2 > numero_3:
    print('Ordem: 1, 2, 3: ', numero_1, numero_2, numero_3)
elif numero_1 > numero_3 > numero_2:
    print('Ordem: 1, 3, 2: ', numero_1, numero_3, numero_2)
elif numero_2 > numero_1 > numero_3:
    print('Ordem: 2, 1, 3: ', numero_2, numero_1, numero_3)
elif numero_2 > numero_3 > numero_1:
    print('Ordem: 2, 3, 1: ', numero_2, numero_3, numero_1)
elif numero_3 > numero_1 > numero_2:
    print('Ordem: 3, 1, 2: ', numero_3, numero_1, numero_2)
elif numero_3 > numero_2 > numero_1:
    print('Ordem: 3, 2, 1: ', numero_3, numero_2, numero_1)
elif numero_1 == numero_2 > numero_3:
    print('Ordem: 1 e 2 iguais, 3: ', numero_1, numero_2, numero_3)
elif numero_1 == numero_3 > numero_2:
    print('Ordem: 1 e 3 iguais, 2: ', numero_1, numero_3, numero_2)
elif numero_2 == numero_3 > numero_1:
    print('Ordem: 2 e 3 iguais, 1: ', numero_2, numero_3, numero_1)
else:
    print('Ordem: 1, 2 e 3 são iguais: ', numero_1, numero_2, numero_3)
