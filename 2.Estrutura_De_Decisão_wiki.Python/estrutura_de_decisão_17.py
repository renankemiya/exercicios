#  Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe
#  se este ano é ou não bissexto.
ano = int(input('Insira um ano: '))
lista_anos_bissextos = list(range(0, 10000, 4))

for bissexto in lista_anos_bissextos:
    if bissexto == ano:
        print('É um ano bissexto')
