def oi(s):
    """Função que imprime a mensagem 'Alo Mundo' com um str especifico

    :param s:
    :return:
    """
    if s == 'oi':
        print('Alo Mundo')
    elif s != 'oi':
        print('tente novamente')


def cumprimento():
    return 'Alo Mundo'


class Alo:
    caixa = {'oi': 'Alo Mundo'}

    def cumpirmentar_2(self):
        ola = self.caixa['oi']
        return f'{ola}'


if __name__ == '__main__':
    oi('oi')
    mundo = Alo()
    print(cumprimento())
    print(mundo.cumpirmentar_2())

print('Alo Mundo')  # resposta certa, corrigido da internet
