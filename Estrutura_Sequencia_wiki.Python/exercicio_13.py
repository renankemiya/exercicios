class PesoIdealPorGenero:
    def __init__(self, h, genero):
        self.genero = genero
        self.h = h

    def calcular_peso(self):
        if self.genero == 'homem':
            peso_h = (self.h * 72.7) - 58
            return f'O peso ideal é de {peso_h}, H'
        elif self.genero == 'mulher':
            peso_m = (self.h * 62.1) - 44.7
            return f'O peso ideal é de {peso_m}, M'


if __name__ == '__main__':
    peso_ideal_h = PesoIdealPorGenero(1.80, 'homem')
    print(peso_ideal_h.calcular_peso())
    peso_ideal_m = PesoIdealPorGenero(1.80, 'mulher')
    print(peso_ideal_m.calcular_peso())
