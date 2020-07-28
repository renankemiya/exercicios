pergunta_a = input('Telefonou para a vítima?, responda sim ou não: ')
pergunta_b = input('Esteve no local do crime?, responda sim ou não: ')
pergunta_c = input('Mora perto da vítima?, responda sim ou não: ')
pergunta_d = input('Devia para a vítima?, responda sim ou não: ')
pergunta_e = input('Já trabalhou com a vítima?, responda sim ou não: ')
respostas_positivas = 0

if pergunta_a == 'sim':
    respostas_positivas += 1
if pergunta_b == 'sim':
    respostas_positivas += 1
if pergunta_c == 'sim':
    respostas_positivas += 1
if pergunta_d == 'sim':
    respostas_positivas += 1
if pergunta_e == 'sim':
    respostas_positivas += 1

if respostas_positivas < 2:
    print('Classificação: Inocente')
elif respostas_positivas == 2:
    print('Classificação: Suspeita')
elif 2 < respostas_positivas < 5:
    print('Classificação: Cúmplice')
else:
    print('Classificação: Assassino')
