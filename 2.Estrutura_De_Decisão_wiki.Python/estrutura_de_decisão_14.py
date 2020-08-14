#  Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre,
#  e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
#   Média de Aproveitamento  Conceito
#   Entre 9.0 e 10.0        A
#   Entre 7.5 e 9.0         B
#   Entre 6.0 e 7.5         C
#   Entre 4.0 e 6.0         D
#   Entre 4.0 e zero        E

nota_1 = float(input('Insira a primeira nota: '))
nota_2 = float(input('Insira a segunda nota: '))
media = (nota_1 + nota_2) / 2

if 4 >= media > 0:
    conceito = 'E'
    print(f'Primeira nota  : {nota_1}')
    print(f'Segunda nota   : {nota_2}')
    print(f'Média          : {media}')
    print(f'Conceito       : {conceito}')
    print('REPROVADO')
elif 6 >= media > 4:
    conceito = 'D'
    print(f'Primeira nota  : {nota_1}')
    print(f'Segunda nota   : {nota_2}')
    print(f'Média          : {media}')
    print(f'Conceito       : {conceito}')
    print('REPROVADO')
elif 7.5 >= media > 6:
    conceito = 'C'
    print(f'Primeira nota  : {nota_1}')
    print(f'Segunda nota   : {nota_2}')
    print(f'Média          : {media}')
    print(f'Conceito       : {conceito}')
    print('APROVADO')
elif 9 >= media > 7.5:
    conceito = 'B'
    print(f'Primeira nota  : {nota_1}')
    print(f'Segunda nota   : {nota_2}')
    print(f'Média          : {media}')
    print(f'Conceito       : {conceito}')
    print('APROVADO')
elif 10 >= media > 9:
    conceito = 'A'
    print(f'Primeira nota  : {nota_1}')
    print(f'Segunda nota   : {nota_2}')
    print(f'Média          : {media}')
    print(f'Conceito       : {conceito}')
    print('APROVADO')

# Correção da internet

nota1 = float(input("Digite o valor da 1ª nota: "))
nota2 = float(input("Digite o valor da 2ª nota: "))

media = (nota1 + nota2) / 2

if 6 <= media <= 7.5:
    print("1ª nota: ", nota1)
    print("2ª nota: ", nota2)
    print("Sua média final é ", media)
    print("Você está aprovado!")
    print("Conceito C")
elif 7.5 <= media <= 9:
    print("1ª nota: ", nota1)
    print("2ª nota: ", nota2)
    print("Sua média final é ", media)
    print("Você está aprovado!")
    print("Conceito B")
elif 9 <= media <= 10:
    print("1ª nota: ", nota1)
    print("2ª nota: ", nota2)
    print("Sua média final é ", media)
    print("Você está aprovado!")
    print("Conceito A")
elif 4 <= media <= 6:
    print("1ª nota: ", nota1)
    print("2ª nota: ", nota2)
    print("Sua média final é ", media)
    print("Você está reprovado!")
    print("Conceito D")
elif 0 <= media <= 4:
    print("1ª nota: ", nota1)
    print("2ª nota: ", nota2)
    print("Sua média final é ", media)
    print("Você está reprovado!")
    print("Conceito E")
