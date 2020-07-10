def oi(s):
    '''Função que imprime a mensagem 'Alo Mundo' com um str especifico

    :param s:
    :return:
    '''
    if s == 'oi':
        print('Alo Mundo')
    elif s != 'oi':
        print('tente novamente')


if __name__ == '__main__':
    oi('oi')
else:
    print(__name__)