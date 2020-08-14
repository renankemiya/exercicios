#  Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# Álcool:
# até 20 litros, desconto de 3% por litro
# acima de 20 litros, desconto de 5% por litro
# Gasolina:
# até 20 litros, desconto de 4% por litro
# acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos,
# o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago
# pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

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
