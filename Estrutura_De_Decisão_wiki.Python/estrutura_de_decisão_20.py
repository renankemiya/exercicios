nota_1 = float(input('Insira a primeira nota: '))
nota_2 = float(input('Insira a segunda nota: '))
nota_3 = float(input('Insira a terceira nota: '))
media = (nota_1 + nota_2 + nota_3) / 3

if media == 10:
    print(f'Aprovado com Distinção: {media}')
elif 7 < media < 10:
    print(f'Aprovado: {media}')
elif media < 7:
    print(f'Reprovado: {media}')
