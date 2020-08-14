#  O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#                       Até 5 Kg           Acima de 5 Kg
# File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
# Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
# Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
# Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não
# há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda
# um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada
# pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total,
# tipo de pagamento, valor do desconto e valor a pagar.

pedido = input('Insira o tipo de carne que deseja, File Duplo, Alcatra ou Picanha: ')

preco_file_duplo1 = 4.90
preco_file_duplo2 = 5.80
preco_alcatra1 = 5.90
preco_alcatra2 = 6.80
preco_picanha1 = 6.90
preco_picanha2 = 7.80

if pedido == 'File Duplo':
    peso = float(input('Insira o peso em Kg que deseja comprar: '))
    if peso <= 5:
        preco = peso * preco_file_duplo1
        cartao = input('Deseja usar o cartão Tabajara?, responda sim ou não: ')
        if cartao == 'sim':
            pagamento = 'Cartão Tabajara'
            desconto = preco * 0.05
            preco_total = preco - desconto
            print(f'Tipo             :{pedido}')
            print(f'Quantidade       :{peso} Kg')
            print(f'Preço Total      :R$ {round(preco,2)} reais')
            print(f'Pagamento        :{pagamento}')
            print(f'(-) Desconto     :R$ {round(desconto,2)} reais')
            print(f'Total a pagar    :R$ {round(preco_total,2)} reais')
        else:
            pagamento = 'A vista'
            print(f'Tipo             :{pedido}')
            print(f'Quantidade       :{peso} Kg')
            print(f'Pagamento        :{pagamento}')
            print(f'Total a pagar    :R$ {round(preco,2)} reais')
    else:
        preco = peso * preco_file_duplo2
        cartao = input('Deseja usar o cartão Tabajara?, responda sim ou não: ')
        if cartao == 'sim':
            pagamento = 'Cartão Tabajara'
            desconto = preco * 0.05
            preco_total = preco - desconto
            print(f'Tipo             :{pedido}')
            print(f'Quantidade       :{peso} Kg')
            print(f'Preço Total      :R$ {round(preco,2)} reais')
            print(f'Pagamento        :{pagamento}')
            print(f'(-) Desconto     :R$ {round(desconto,2)} reais')
            print(f'Total a pagar    :R$ {round(preco_total,2)} reais')
        else:
            pagamento = 'A vista'
            print(f'Tipo             :{pedido}')
            print(f'Quantidade       :{peso} Kg')
            print(f'Pagamento        :{pagamento}')
            print(f'Total a pagar    :R$ {round(preco,2)} reais')


elif pedido == 'Alcatra':
    peso = float(input('Insira o peso em Kg que deseja comprar: '))
    if peso <= 5:
        preco = peso * preco_alcatra1
        cartao = input('Deseja usar o cartão Tabajara?, responda sim ou não: ')
        if cartao == 'sim':
            pagamento = 'Cartão Tabajara'
            desconto = preco * 0.05
            preco_total = preco - desconto
            print(f'Tipo             :{pedido}')
            print(f'Quantidade       :{peso} Kg')
            print(f'Preço Total      :R$ {round(preco,2)} reais')
            print(f'Pagamento        :{pagamento}')
            print(f'(-) Desconto     :R$ {round(desconto,2)} reais')
            print(f'Total a pagar    :R$ {round(preco_total,2)} reais')
        else:
            pagamento = 'A vista'
            print(f'Tipo             :{pedido}')
            print(f'Quantidade       :{peso} Kg')
            print(f'Pagamento        :{pagamento}')
            print(f'Total a pagar    :R$ {round(preco,2)} reais')
    else:
        preco = peso * preco_alcatra2
        cartao = input('Deseja usar o cartão Tabajara?, responda sim ou não: ')
        if cartao == 'sim':
            pagamento = 'Cartão Tabajara'
            desconto = preco * 0.05
            preco_total = preco - desconto
            print(f'Tipo             :{pedido}')
            print(f'Quantidade       :{peso} Kg')
            print(f'Preço Total      :R$ {round(preco,2)} reais')
            print(f'Pagamento        :{pagamento}')
            print(f'(-) Desconto     :R$ {round(desconto,2)} reais')
            print(f'Total a pagar    :R$ {round(preco_total,2)} reais')
        else:
            pagamento = 'A vista'
            print(f'Tipo             :{pedido}')
            print(f'Quantidade       :{peso} Kg')
            print(f'Pagamento        :{pagamento}')
            print(f'Total a pagar    :R$ {round(preco,2)} reais')

elif pedido == 'Picanha':
    peso = float(input('Insira o peso em Kg que deseja comprar: '))
    if peso <= 5:
        preco = peso * preco_picanha1
        cartao = input('Deseja usar o cartão Tabajara?, responda sim ou não: ')
        if cartao == 'sim':
            pagamento = 'Cartão Tabajara'
            desconto = preco * 0.05
            preco_total = preco - desconto
            print(f'Tipo             :{pedido}')
            print(f'Quantidade       :{peso} Kg')
            print(f'Preço Total      :R$ {round(preco,2)} reais')
            print(f'Pagamento        :{pagamento}')
            print(f'(-) Desconto     :R$ {round(desconto,2)} reais')
            print(f'Total a pagar    :R$ {round(preco_total,2)} reais')
        else:
            pagamento = 'A vista'
            print(f'Tipo             :{pedido}')
            print(f'Quantidade       :{peso} Kg')
            print(f'Pagamento        :{pagamento}')
            print(f'Total a pagar    :R$ {round(preco,2)} reais')
    else:
        preco = peso * preco_picanha2
        cartao = input('Deseja usar o cartão Tabajara?, responda sim ou não: ')
        if cartao == 'sim':
            pagamento = 'Cartão Tabajara'
            desconto = preco * 0.05
            preco_total = preco - desconto
            print(f'Tipo             :{pedido}')
            print(f'Quantidade       :{peso} Kg')
            print(f'Preço Total      :R$ {round(preco,2)} reais')
            print(f'Pagamento        :{pagamento}')
            print(f'(-) Desconto     :R$ {round(desconto,2)} reais')
            print(f'Total a pagar    :R$ {round(preco_total,2)} reais')
        else:
            pagamento = 'A vista'
            print(f'Tipo             :{pedido}')
            print(f'Quantidade       :{peso} Kg')
            print(f'Pagamento        :{pagamento}')
            print(f'Total a pagar    :R$ {round(preco,2)} reais')

else:
    print('Esse pedido é inválido')
