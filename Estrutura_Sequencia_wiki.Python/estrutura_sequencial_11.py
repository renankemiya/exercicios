class Calculador:
    def __init__(self, inteiro_1, inteiro_2, real):
        self.real = real
        self.inteiro_2 = inteiro_2
        self.inteiro_1 = inteiro_1

    def calculo_a(self):
        dobro_de_i1 = self.inteiro_1 * 2
        metade_do_i2 = (self.inteiro_2 / 2)
        produto = dobro_de_i1 * metade_do_i2
        return f'resultado A: {produto}'

    def calculo_b(self):
        triplo_de_i1 = self.inteiro_1 * 3
        soma = triplo_de_i1 + self.real
        return f'resultado B: {soma}'

    def calculo_c(self):
        valor = self.real ** 3
        return f'resultado C: {valor}'

    def calculos_abc(self):
        dobro_de_i1 = self.inteiro_1 * 2
        metade_do_i2 = (self.inteiro_2 / 2)
        produto = dobro_de_i1 * metade_do_i2
        triplo_de_i1 = self.inteiro_1 * 3
        soma = triplo_de_i1 + self.real
        valor = self.real ** 3
        return f'resultado A: {produto}, resultado B: {soma}, resultado C: {valor}'


if __name__ == '__main__':
    calculador = Calculador(3, 40, 8)
    print(calculador.calculo_a())
    print(calculador.calculo_b())
    print(calculador.calculo_c())
    print(calculador.calculos_abc())

x1 = int(input('Informe o primeiro número inteiro: '))  # resposta certa, corrigido da internet
x2 = int(input('Informe o segundo número inteiro: '))
r = float(input('Informe um número real: '))

a = (2 * x1) * (x2 / 2)
b = 3 * x1 + r
c = r ** 3

print(a)
print(b)
print(c)
