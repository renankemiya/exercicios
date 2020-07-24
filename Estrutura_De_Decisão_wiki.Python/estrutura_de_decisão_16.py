a = int(input('Insira um número: '))
if a == 0:
    print('Isso não é uma equação de segundo grau')
else:
    b = int(input('Insira outro número: '))
    c = int(input('Insira outro número: '))
    delta = (b**2)-(4*a*c)
    if delta < 0:
        print('A equação não possui raizes reais')
    elif delta == 0:
        resultado = -b/(2*a)
        print(f'A equação possui apenas uma raiz real: {resultado}')
    elif delta > 0:
        resultado_1 = (-b+(delta**0.5))/(2*a)
        resultado_2 = (-b-(delta**0.5))/(2*a)
        print(f'A equação possui duas raizes reais: {resultado_1} e {resultado_2}')
