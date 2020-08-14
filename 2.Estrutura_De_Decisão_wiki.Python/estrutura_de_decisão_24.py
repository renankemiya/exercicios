#  Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
#  O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
# par ou ímpar;
# positivo ou negativo;
# inteiro ou decimal.

numero_1 = float(input('Insira um número: '))
numero_2 = float(input('Insira outro número: '))
operacao = input('Insira a operação que deseja realizar: somar, subtrair, dividir ou multiplicar: ')
resultado = 0

if operacao == 'somar':
    resultado = numero_1 + numero_2
elif operacao == 'subtrair':
    resultado = numero_1 - numero_2
elif operacao == 'dividir':
    resultado = numero_1 / numero_2
elif operacao == 'multiplicar':
    resultado = numero_1 * numero_2
else:
    print('Essa opereção é inválida, tente novamente')

resto = resultado % 2
checar_decimal = round(resultado)

if resto == 0:
    if resultado == checar_decimal:
        if resultado > 0:
            print(f'O resultado da operação {operacao} foi {resultado}')
            print(f'a. É um número par')
            print(f'b. É um número positivo')
            print(f'c. É um número inteiro')
        elif resultado < 0:
            print(f'O resultado da operação {operacao} foi {resultado}')
            print(f'a. É um número par')
            print(f'b. É um número negativo')
            print(f'c. É um número inteiro')
        else:
            print(f'O resultado da operação {operacao} foi {resultado}')
            print(f'a. É um número par')
            print(f'b. É igual a 0')
            print(f'c. É um número inteiro')
    else:
        if resultado > 0:
            print(f'O resultado da operação {operacao} foi {resultado}')
            print(f'a. É um número par')
            print(f'b. É um número positivo')
            print(f'c. É um número decimal')
        elif resultado < 0:
            print(f'O resultado da operação {operacao} foi {resultado}')
            print(f'a. É um número par')
            print(f'b. É um número negativo')
            print(f'c. É um número decimal')
        else:
            print(f'O resultado da operação {operacao} foi {resultado}')
            print(f'a. É um número par')
            print(f'b. É igual a 0')
            print(f'c. É um número decimal')
else:
    if resultado == checar_decimal:
        if resultado > 0:
            print(f'O resultado da operação {operacao} foi {resultado}')
            print(f'a. É um número impar')
            print(f'b. É um número positivo')
            print(f'c. É um número inteiro')
        elif resultado < 0:
            print(f'O resultado da operação {operacao} foi {resultado}')
            print(f'a. É um número impar')
            print(f'b. É um número negativo')
            print(f'c. É um número inteiro')
        else:
            print(f'O resultado da operação {operacao} foi {resultado}')
            print(f'a. É um número impar')
            print(f'b. É igual a 0')
            print(f'c. É um número inteiro')
    else:
        if resultado > 0:
            print(f'O resultado da operação {operacao} foi {resultado}')
            print(f'a. É um número impar')
            print(f'b. É um número positivo')
            print(f'c. É um número decimal')
        elif resultado < 0:
            print(f'O resultado da operação {operacao} foi {resultado}')
            print(f'a. É um número impar')
            print(f'b. É um número negativo')
            print(f'c. É um número decimal')
        else:
            print(f'O resultado da operação {operacao} foi {resultado}')
            print(f'a. É um número impar')
            print(f'b. É igual a 0')
            print(f'c. É um número decimal')
