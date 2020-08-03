#  Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
#  Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

turno = input('Insira o turno que você estuda, digite M para Matutino, V para Vespertino e N para Noturno: ')

if turno == 'M':
    print('Bom Dia!')
elif turno == 'V':
    print('Boa Tarde!')
elif turno == 'N':
    print('Boa Noite!')
else:
    print('Valor Inválido!')

# Correção da internet

turno = input("digite seu turno M-matutino ou V-Vespertino ou N- Noturno ---> ")
if turno == "M" or turno == "m":
    print("bom dia")
if turno == "V" or turno == "v":
    print("boa tarde")
if turno == "N" or turno == "n":
    print("boa noite")
