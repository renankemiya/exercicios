#  Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores
#  podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
# Dicas:
# Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
# Triângulo Equilátero: três lados iguais;
# Triângulo Isósceles: quaisquer dois lados iguais;
# Triângulo Escaleno: três lados diferentes;

t_lado1 = float(input('Insira um lado do triângulo: '))
t_lado2 = float(input('Insira outro lado do triângulo: '))
t_lado3 = float(input('Insira o último lado do triângulo: '))

if t_lado1 >= t_lado2 + t_lado3 or t_lado2 >= t_lado1 + t_lado3 or t_lado3 >= t_lado1 + t_lado2:
    print('Os lados inseridos não podem ser um triângulo')
elif t_lado1 == t_lado2 == t_lado3:
    print('Esse triângulo é um Equilátero')
elif t_lado1 == t_lado2 or t_lado1 == t_lado3 or t_lado2 == t_lado3:
    print('Esse triângulo é um Isósceles')
elif t_lado1 != t_lado2 != t_lado3:
    print('Esse triângulo é um Escaleno')

#  Correção da internet
print("| Verifique se é um triângulo e qual seu tipo | ")

lado1 = float(input(" Digite o valor do primeiro lado: "))
lado2 = float(input(" Digite o valor do segundo lado: "))
lado3 = float(input(" Digite o valor do terceiro lado: "))

if (lado1 + lado2) > lado3:
    if lado1 == lado2 and lado2 == lado3 and lado1 == lado3:
        print(" Triângulo Equilátero")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print(" Triângulo Isósceles")
    elif lado1 != lado2 and lado3 or lado2 != lado1 and lado3:
        print(" Triângulo Escaleno")
else:
    print(" Os valores informados não correspondem a um triângulo")
