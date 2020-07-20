class PesoIdeal:
    def __init__(self, altura_c):
        self.altura = altura_c

    def calcular_peso_ideal(self):
        peso_c = self.altura * 72.7
        peso_c = peso_c - 58
        return f'O peso ideal é de {peso_c} Kg'


if __name__ == '__main__':
    peso = PesoIdeal(2.10)
    print(peso.calcular_peso_ideal())

altura = float(input('Informe sua altura: '))  # resposta certa, corrigido da internet

peso = 72.7 * altura - 58

print('Seu peso ideal seria: ', peso, 'Kg')
