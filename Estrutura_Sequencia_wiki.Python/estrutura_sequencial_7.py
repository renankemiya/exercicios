class AreaDobradaDoQuadrado:
    """ Classe que guarda o calculo da area do quadrado dobrado
    
    """

    def __init__(self, lado):
        self.lado = lado

    def calcular_area_quadrado(self):
        lado_do_quadrado = self.lado ** 2
        lado_do_quadrado = lado_do_quadrado * 2
        return f'area do quadrado dobrada = {lado_do_quadrado}'


def calcular_area_dobrada_quadrado(lado):
    area_dobrada = (lado ** 2) * 2
    return f'area do quadrado dobrada = {area_dobrada}'


if __name__ == '__main__':
    areaX2 = AreaDobradaDoQuadrado(10)
    print(areaX2.calcular_area_quadrado())
    print(calcular_area_dobrada_quadrado(20))

