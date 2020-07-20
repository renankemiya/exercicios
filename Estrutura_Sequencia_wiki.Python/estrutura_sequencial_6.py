import math


class CalcularAreaDoCirculo:
    area_do_circulo = 0

    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        raio = self.raio
        resultado = (raio ** 2) * math.pi
        return f'area do circulo = {resultado}'


def calcular_area_circulo(raio):
    area = (raio ** 2) * math.pi
    return f'area do circulo = {area}'


if __name__ == '__main__':
    area_do_circulo = CalcularAreaDoCirculo(5)
    print(area_do_circulo.calcular_area())
    print((calcular_area_circulo(10)))
