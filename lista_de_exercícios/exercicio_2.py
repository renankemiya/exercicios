def chamar_numero(s):
    '''Função que pede um número com uma str especifica e retorna o número digitado com uma frase

    :param s:
    :return:
    '''
    if s == 1:
        resultado = (input('Digite um número:'))
        print(f'O número informado foi {resultado}')
    elif s != 1:
        print('tente novamente')


if __name__ == '__main__':
    chamar_numero(1)
else:
    print(__name__)
