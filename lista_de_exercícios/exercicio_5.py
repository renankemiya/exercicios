class Conversor:
    """ CLasse que guarda o calculo de convrsão de metro para centimetros

    """
    def __init__(self, metro):
        self.metro = metro

    def conversor(self):
        return self.metro * 100

def metros_para_centimetros(s):
    """ Função que converte metros para centimetros

    :param s:
    :return:
    """
    return s * 100

if __name__ == '__main__':
    valor = Conversor(1)
    print(valor.conversor())
    valor.metro = 10
    print(valor.conversor())
    print(metros_para_centimetros(1))
