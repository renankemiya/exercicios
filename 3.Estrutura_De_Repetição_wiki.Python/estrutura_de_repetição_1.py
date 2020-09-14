#  Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue
#  pedindo até que o usuário informe um valor válido.

nota = float(input('Insira um nota entre 0 a 10: '))

while nota < 0 or nota > 10:
    print('Nota Inválida')
    nota = float(input('Insira um nota entre 0 a 10: '))

if nota >= 0 or nota <= 10:
    print('Nota Válida', nota)
