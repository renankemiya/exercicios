class AreaDobradaDoQuadrado:
    """ Classe que guarda o calculo da area do quadrado dobrado
    
    """

    def __init__(self, lado):
        self.lado = lado

    def calcular_area_quadrado(self):
        lado_do_quadrado = self.lado ** 2
        return lado_do_quadrado * 2


def calcular_area_dobrada_quadrado(lado):
    area_dobrada = (lado ** 2) * 2
    return area_dobrada


if __name__ == '__main__':
    areaX2 = AreaDobradaDoQuadrado(10)
    print(areaX2.calcular_area_quadrado())
    print(calcular_area_dobrada_quadrado(20))
