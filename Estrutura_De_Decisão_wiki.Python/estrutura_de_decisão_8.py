preco_1 = float(input('Insira o primeiro preço: '))
preco_2 = float(input('Insira o segundo preço: '))
preco_3 = float(input('Insira o terceiro preço: '))

if preco_1 < preco_2:
    if preco_1 < preco_3:
        print(f'O primeiro preço é o menor: {preco_1}')
    elif preco_1 > preco_3:
        print(f'o terceiro preço é o menor: {preco_3}')
    else:
        print(f'O primeiro e o terceiro tem o mesmo preço: {preco_1}, {preco_3}')
elif preco_2 < preco_3:
    if preco_2 < preco_1:
        print(f'O segundo preço é o menor: {preco_2}')
    elif preco_2 > preco_1:
        print(f'o primeiro preço é o menor: {preco_1}')
    else:
        print(f'O segundo e o primeiro tem o mesmo preço: {preco_2}, {preco_1}')
elif preco_3 < preco_1:
    if preco_3 < preco_2:
        print(f'O terceiro preço é o menor: {preco_3}')
    elif preco_3 > preco_2:
        print(f'o segundo preço é o menor: {preco_2}')
    else:
        print(f'O terceiro e o segundo tem o mesmo preço: {preco_3}, {preco_2}')
else:
    print(f'Existem preços iguais: {preco_1}, {preco_2}, {preco_3}')
