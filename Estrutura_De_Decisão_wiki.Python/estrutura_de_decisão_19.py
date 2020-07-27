ler_numero = int(input('Insira um número menor que 1000: '))

if ler_numero < 10:
    numero = str(ler_numero)
    unidade = numero[0]
    if int(unidade) < 2:
        p_unidade = 'unidade'
    else:
        p_unidade = 'unidades'
    print(f'{ler_numero} = {unidade} {p_unidade}')
elif ler_numero < 100:
    numero = str(ler_numero)
    dezena = numero[0]
    unidade = numero[1]
    if int(dezena) < 2:
        p_dezena = 'dezena'
    else:
        p_dezena = 'dezenas'
    if int(unidade) < 2:
        p_unidade = 'unidade'
    else:
        p_unidade = 'unidades'
    print(f'{ler_numero} = {dezena} {p_dezena} e {unidade} {p_unidade}')
elif ler_numero < 1000:
    numero = str(ler_numero)
    centena = numero[0]
    dezena = numero[1]
    unidade = numero[2]
    if int(centena) < 2:
        p_centena = 'centena'
    else:
        p_centena = 'centenas'
    if int(dezena) < 2:
        p_dezena = 'dezena'
    else:
        p_dezena = 'dezenas'
    if int(unidade) < 2:
        p_unidade = 'unidade'
    else:
        p_unidade = 'unidades'
    print(f'{ler_numero} = {centena} {p_centena}, {dezena} {p_dezena} e {unidade} {p_unidade}')
else:
    print('Esse número é inválido')
# 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
