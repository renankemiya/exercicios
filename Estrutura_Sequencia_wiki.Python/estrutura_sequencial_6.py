import math


class CalcularAreaDoCirculo:
    area_do_circulo = 0

    def __init__(self, raio_c):
        self.raio_c = raio_c

    def calcular_area(self):
        raio_f = self.raio_c
        resultado = (raio_f ** 2) * math.pi
        return f'area do circulo = {resultado}'


def calcular_area_circulo(raio_f):
    area_f = (raio_f ** 2) * math.pi
    return f'area do circulo = {area_f}'


if __name__ == '__main__':
    area_do_circulo = CalcularAreaDoCirculo(5)
    print(area_do_circulo.calcular_area())
    print((calcular_area_circulo(10)))

raio = int(input('Qual a medida do raio do circulo?: '))  # resposta certa, corrigida da internet

area = 3.1415 * raio ** 2

print('A area desse circulo é: ', area)
