#  Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação
# da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
# entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

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
