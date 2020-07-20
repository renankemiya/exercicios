class ConversorParaCentimetros:
    """ CLasse que guarda o calculo de conversão de distancia para centimetros

    """

    def __init__(self, metro_c):
        self.metro_c = metro_c

    def conversor_para_centimetros(self):
        metro_c = self.metro_c * 100
        return f'{metro_c} centimetros'


def metros_para_centimetros(s):
    """ Função que converte metros para centimetros

    :param s:
    :return:
    """
    valor_f = s * 100
    return f'{valor_f} centimetros'


if __name__ == '__main__':
    valor = ConversorParaCentimetros(1)
    print(valor.conversor_para_centimetros())
    valor.metro = 10
    print(valor.conversor_para_centimetros())
    print(metros_para_centimetros(1))

metro = int(input('Insira a sua medida em metros: '))  # resposta certa, corrigido da internet

cm = metro * 100

print('Sua medida em centimetros é: ', cm, 'cm')
