saque = int(input('Insira a quantidade que deseja sacar: '))

nota_de_1 = 0
nota_de_5 = 0
nota_de_10 = 0
nota_de_50 = 0
nota_de_100 = 0

if 10 <= saque <= 600:
    saque_salvo = saque
    n_100 = 'nenhuma nota de 100'
    n_50 = 'nenhuma nota de 50'
    n_10 = 'nenhuma nota de 10'
    n_5 = 'nenhuma nota de 5'
    n_1 = 'nenhuma nota de 1'
    while saque >= 100:
        saque -= 100
        nota_de_100 += 1
        if nota_de_100 == 1:
            n_100 = f'{nota_de_100} nota de 100 reais'
        else:
            n_100 = f'{nota_de_100} notas de 100 reais'
    while saque >= 50:
        saque -= 50
        nota_de_50 += 1
        if nota_de_50 == 1:
            n_50 = f'{nota_de_50} nota de 50 reais'
        else:
            n_50 = f'{nota_de_50} notas de 50 reais'
    while saque >= 10:
        saque -= 10
        nota_de_10 += 1
        if nota_de_10 == 1:
            n_10 = f'{nota_de_10} nota de 10 reais'
        else:
            n_10 = f'{nota_de_10} notas de 10 reais'
    while saque >= 5:
        saque -= 5
        nota_de_5 += 1
        if nota_de_5 == 1:
            n_5 = f'{nota_de_5} nota de 5 reais'
        else:
            n_5 = f'{nota_de_5} notas de 5 reais'
    while saque >= 1:
        saque -= 1
        nota_de_1 += 1
        if nota_de_1 == 1:
            n_1 = f'{nota_de_1} nota de 1 real'
        else:
            n_1 = f'{nota_de_1} notas de 1 real'
    print(f'Você sacou {saque_salvo}')
    print(f'Notas recebidas:')
    print(f'{n_100}')
    print(f'{n_50}')
    print(f'{n_10}')
    print(f'{n_5}')
    print(f'{n_1}')

else:
    print('Esse valor é inválido')
