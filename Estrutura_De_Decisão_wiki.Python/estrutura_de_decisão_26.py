comprar = input('Escolha A para álcool ou G para Gasolina: ')

if comprar == 'A':
    quantidade = float(input('Insira a quantidade que deseja comprar: '))
    valor_por_litro = 1.90
    desconto_ate_20 = valor_por_litro * 0.03
    desconto_maior_que_20 = valor_por_litro * 0.05
    if quantidade <= 20:
        pagamento_bruto = quantidade * valor_por_litro
        desconto_total = quantidade * desconto_ate_20
        pagamento_total = pagamento_bruto - desconto_total
        print(f'{quantidade} litros de Álcool custam {round(pagamento_total,2)} Reais')
    else:
        pagamento_bruto = quantidade * valor_por_litro
        desconto_total = quantidade * desconto_maior_que_20
        pagamento_total = pagamento_bruto - desconto_total
        print(f'{quantidade} litros de Álcool custam {round(pagamento_total,2)} Reais')
elif comprar == 'G':
    quantidade = float(input('Insira a quantidade que deseja comprar: '))
    valor_por_litro = 2.50
    desconto_ate_20 = valor_por_litro * 0.04
    desconto_maior_que_20 = valor_por_litro * 0.06
    if quantidade <= 20:
        pagamento_bruto = quantidade * valor_por_litro
        desconto_total = quantidade * desconto_ate_20
        pagamento_total = pagamento_bruto - desconto_total
        print(f'{quantidade} litros de Gasolina custam {round(pagamento_total,2)} Reais')
    else:
        pagamento_bruto = quantidade * valor_por_litro
        desconto_total = quantidade * desconto_maior_que_20
        pagamento_total = pagamento_bruto - desconto_total
        print(f'{quantidade} litros de Gasolina custam {round(pagamento_total,2)} Reais')
