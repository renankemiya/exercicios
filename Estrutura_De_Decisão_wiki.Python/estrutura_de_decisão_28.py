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
