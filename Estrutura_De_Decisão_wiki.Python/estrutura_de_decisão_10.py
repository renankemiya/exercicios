turno = input('Insira o turno que você estuda, digite M para Matutino, V para Vespertino e N para Noturno: ')

if turno == 'M':
    print('Bom Dia!')
elif turno == 'V':
    print('Boa Tarde!')
elif turno == 'N':
    print('Boa Noite!')
else:
    print('Valor Inválido!')
