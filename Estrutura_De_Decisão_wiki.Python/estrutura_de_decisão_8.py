preco_1 = float(input('Insira o primeiro preço: '))
preco_2 = float(input('Insira o segundo preço: '))
preco_3 = float(input('Insira o terceiro preço: '))

if preco_1 < preco_2 < preco_3:
    print(f'O menor preço é o do primeiro: {preco_1}')
elif preco_1 < preco_2 > preco_3:
    print(f'O menor preço é o do primeiro: {preco_1}')
elif preco_2 < preco_3 < preco_1:
    print(f'O menor preço é o do segundo: {preco_2}')
elif preco_2 < preco_3 > preco_1:
    print(f'O menor preço é o do segundo: {preco_2}')
elif preco_3 < preco_1 < preco_2:
    print(f'O menor preço é o do terceiro: {preco_3}')
elif preco_3 < preco_1 > preco_2:
    print(f'O menor preço é o do terceiro: {preco_3}')
else:
    print('Existem preços iguais')
