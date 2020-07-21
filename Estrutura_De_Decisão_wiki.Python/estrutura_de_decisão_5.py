nota_1 = float(input('Insira a nota: '))
nota_2 = float(input('Insira outro número: '))
media = (nota_1 + nota_2) / 2


if media == 10:
    print('Aprovado com Distinção')
elif media >= 7:
    print('Aprovado')
elif media < 7:
    print('Reprovado')
