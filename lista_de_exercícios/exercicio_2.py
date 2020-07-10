def chamar_numero(s):
    '''Função que pede um número e informa o número que foi colocado

    :param s:
    :return:
    '''
    if s == 1:
        resultado = (input('Digite um número:'))
        print(resultado)
    elif s != 1:
        print('tente novamente')


if __name__ == '__main__':
    chamar_numero(1)
else:
    print(__name__)
