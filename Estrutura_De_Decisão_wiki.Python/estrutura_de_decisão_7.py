numero_1 = float(input('Insira o primeiro número: '))
numero_2 = float(input('Insira o segundo número: '))
numero_3 = float(input('Insira o terceiro número: '))

if numero_1 > numero_2:
    if numero_1 > numero_3:
        if numero_2 > numero_3:
            print(f'O primeiro é o maior: {numero_1}, e o terceiro é o menor: {numero_3}')
        elif numero_2 < numero_3:
            print(f'O primeiro é o maior: {numero_1}, o segundo é o menor: {numero_2}')
        else:
            print(f'O primeiro é o ')
    elif numero_1 < numero_3:
        print(f'O terceiro é o maior número {numero_3}')
    else:
        print(f'O primeiro e o terceiro são iguais: {numero_1}, {numero_3}')
elif numero_2 > numero_3:
    if numero_2 > numero_1:
        print(f'O segundo é o maior número: {numero_2}')
    elif numero_2 < numero_1:
        print(f'O primeiro é o maior número: {numero_1}')
    else:
        print(f'O segundo e o primeiro são iguais: {numero_2}, {numero_1}')
elif numero_3 > numero_1:
    if numero_3 > numero_2:
        print(f'O terceiro é o maior número: {numero_3}')
    elif numero_3 < numero_2:
        print(f'O segundo é o maior número: {numero_2}')
    else:
        print(f'O terceiro e o segundo são iguais: {numero_3}, {numero_2}')
else:
    print(f'Todos os números são iguais: {numero_1}, {numero_2}, {numero_3}')
