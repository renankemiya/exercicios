def chamar_numero(s):
    '''Função que pede um número com uma str especifica e retorna o número digitado com uma frase, primeira tentativa

    :param s:
    :return:
    '''
    if s == 1:
        resultado = (input('Digite um número:'))
        print(f'O número informado foi {resultado}')
    elif s != 1:
        print('tente novamente')

class Mandar():

    def __init__(self, numero = 0):
        self.numero = numero


    def envio(self, frase = 'O numero informado foi'):
        self.frase = frase
        return f'{self.frase} {self.numero}'



if __name__ == '__main__':
    mandar = Mandar()
    mandar.numero = 100
    print(mandar.envio())
    chamar_numero(1)
else:
    print(__name__)
