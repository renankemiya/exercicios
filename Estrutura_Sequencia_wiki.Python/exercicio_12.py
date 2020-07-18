class PesoIdeal:
    def __init__(self, altura):
        self.altura = altura

    def calcular_peso_ideal(self):
        peso = self.altura * 72.7
        peso = peso - 58
        return f'O peso ideal é de {peso} Kg'

if __name__ == '__main__':
    peso = PesoIdeal(2.10)
    print(peso.calcular_peso_ideal())