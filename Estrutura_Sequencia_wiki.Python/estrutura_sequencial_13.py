#  Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
#  utilizando as seguintes fórmulas:
#  a. Para homens: (72.7*h) - 58
#  b. Para mulheres: (62.1*h) - 44.7


class PesoIdealPorGenero:
    def __init__(self, h, genero):
        self.genero = genero
        self.h = h

    def calcular_peso(self):
        if self.genero == 'homem':
            peso_h = int((self.h * 72.7) - 58)
            return f'O peso ideal é de {peso_h} Kg, H'
        elif self.genero == 'mulher':
            peso_m = int((self.h * 62.1) - 44.7)
            return f'O peso ideal é de {peso_m} Kg, M'


if __name__ == '__main__':
    peso_ideal_h = PesoIdealPorGenero(1.80, 'homem')
    print(peso_ideal_h.calcular_peso())
    peso_ideal_m = PesoIdealPorGenero(1.80, 'mulher')
    print(peso_ideal_m.calcular_peso())

altura = float(input('Qual a sua altura?: '))  # resposta certa, corrigido da internet
sexo = input('Você é o homem ou mulher?: ')
peso = float(input('Qual o seu peso?: '))

if sexo == 'mulher':
    peso_ideal = (62.1 * altura) - 44.7
    print('Seu peso ideal seria:', peso_ideal)
else:

    peso_ideal = (72.7 * altura) - 58
    print('Seu peso ideal seria:', peso_ideal)

if peso < peso_ideal:
    print('Você está abaixo do seu peso ideal')
elif peso == peso_ideal:
    print('Você está no seu peso ideal')
else:
    print('Você está acima do seu peso ideal ')
