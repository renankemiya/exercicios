#  Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                       Até 5 Kg           Acima de 5 Kg
# Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
# Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25.00,
# receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e
# a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

comprar = input('Insira se deseja comprar apenas maças, apenas moragos ou ambos: ')
ma_preco_ate_5 = 1.80
ma_preco_maior_5 = 1.50
mo_preco_ate_5 = 2.50
mo_preco_maior_5 = 2.20

if comprar == 'maças':
    peso = float(input('Quantidade de maças que deseja comprar em Kg: '))
    if peso <= 5:
        a_pagar = peso * ma_preco_ate_5
        print(f'O valor de {peso} Kg de maças é de {round(a_pagar, 2)} reais')
    else:
        a_pagar = peso * ma_preco_maior_5
        if peso > 8 or a_pagar > 25:
            desconto_total = a_pagar * 0.1
            total_a_pagar = a_pagar - desconto_total
            print(f'O valor de {peso} Kg de maças é de {round(total_a_pagar, 2)} reais')
        else:
            print(f'O valor de {peso} Kg de maças é de {round(a_pagar, 2)} reais')
elif comprar == 'morangos':
    peso = float(input('Quantidade de morangos que deseja comprar em Kg: '))
    if peso <= 5:
        a_pagar = peso * mo_preco_ate_5
        print(f'O valor de {peso} Kg de morangos é de {round(a_pagar, 2)} reais')
    else:
        a_pagar = peso * mo_preco_maior_5
        if peso > 8 or a_pagar > 25:
            desconto_total = a_pagar * 0.1
            total_a_pagar = a_pagar - desconto_total
            print(f'O valor de {peso} Kg de morangos é de {round(total_a_pagar, 2)} reais')
        else:
            print(f'O valor de {peso} Kg de morangos é de {round(a_pagar, 2)} reais')
elif comprar == 'ambos':
    peso_macas = float(input('Quantidade de maças que deseja comprar em Kg: '))
    peso_morangos = float(input('Quantidade de morangos que deseja comprar em Kg: '))
    peso_total = peso_macas + peso_morangos
    if peso_total <= 5:
        preco_total = (peso_macas * ma_preco_ate_5) + (peso_morangos * mo_preco_ate_5)
        print(f'{peso_total} Kg em maças e morangos irão custar {round(preco_total, 2)} reais')
    else:
        preco_total = (peso_macas * ma_preco_maior_5) + (peso_morangos * mo_preco_maior_5)
        if peso_total > 8 or preco_total > 25:
            desconto_geral = preco_total * 0.1
            preco_a_pagar = preco_total - desconto_geral
            print(f'{peso_total} Kg em maças e morangos irão custar {round(preco_a_pagar, 2)} reais')
        else:
            print(f'{peso_total} Kg em maças e morangos irão custar {round(preco_total, 2)} reais')
else:
    print('Opção inválida')
