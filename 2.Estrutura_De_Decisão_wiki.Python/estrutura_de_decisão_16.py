import math
#  Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c.
#  O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário
#  nas seguintes situações:
# Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa
# não deve fazer pedir os demais valores, sendo encerrado;
# Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
# Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
# Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

a = int(input('Insira um número: '))
if a == 0:
    print('Isso não é uma equação de segundo grau')
else:
    b = int(input('Insira outro número: '))
    c = int(input('Insira outro número: '))
    delta = (b ** 2) - (4 * a * c)
    if delta < 0:
        print('A equação não possui raizes reais')
    elif delta == 0:
        resultado = -b / (2 * a)
        print(f'A equação possui apenas uma raiz real: {resultado}')
    elif delta > 0:
        resultado_1 = (-b + (delta ** 0.5)) / (2 * a)
        resultado_2 = (-b - (delta ** 0.5)) / (2 * a)
        print(f'A equação possui duas raizes reais: {round(resultado_1, 2)} e {round(resultado_2, 2)}')

#  Correção da internet


print("| digite os valores correspondente a equação do 2º grau: A, B e C | ")
a = float(input("Digite o valor de A: "))

if a == 0:
    print("A equação não é de 2º grau.")
else:
    b = float(input("Digite o valor de B: "))
    c = float(input("Digite o valor de C: "))

    delta = (b ** 2) - 4 * a * c

    if delta < 0:
        print("A equação não possui raizes reais")
    if delta == 0:
        raiz = ((-1) * b + math.sqrt(delta)) / (2 * a)
        print("Sua equação possui apenas uma raíz, que é igual a ", raiz)
    if delta > 0:
        raiz = ((-1) * b + math.sqrt(delta)) / (2 * a)
        raiz2 = ((-1) * b - math.sqrt(delta)) / (2 * a)
        print("A primeira raiz da equação é igual a ", raiz)
        print("A segunda raiz da equação é igual a ", raiz2)
