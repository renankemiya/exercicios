dia_de_nascimento = int(input('Insira seu dia de nascimento: '))
mes_de_nascimento = int(input('Insira seu mês de nascimento: '))
ano_de_nascimento = int(input('Insira seu ano de nascimento: '))

if dia_de_nascimento > 31:
    print('Esse não é um dia válido')
elif mes_de_nascimento > 12:
    print('Esse não é um mês válido')
elif ano_de_nascimento > 2020:
    print('Esse não é um ano válido')
