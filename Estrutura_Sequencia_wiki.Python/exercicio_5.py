class ConversorParaCentimetros:
    """ CLasse que guarda o calculo de conversão de distancia para centimetros

    """
    def __init__(self, metro):
        self.metro = metro

    def conversor_para_centimetros(self):
        metro = self.metro * 100
        return metro

def metros_para_centimetros(s):
    """ Função que converte metros para centimetros

    :param s:
    :return:
    """
    return s * 100

if __name__ == '__main__':
    valor = ConversorParaCentimetros(1)
    print(valor.conversor_para_centimetros())
    valor.metro = 10
    print(valor.conversor_para_centimetros())
    print(metros_para_centimetros(1))
