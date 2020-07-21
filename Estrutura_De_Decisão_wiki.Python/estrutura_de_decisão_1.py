numero_1 = float(input('Insira um número: '))
numero_2 = float(input('Insira outro número: '))

if numero_1 > numero_2:
    print(f'O primeiro número é maior: {numero_1}')
elif numero_2 > numero_1:
    print(f'O segundo número é maior: {numero_2}')
else:
    print(f'Os números são iguais: {numero_1}')
