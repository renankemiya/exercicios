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
