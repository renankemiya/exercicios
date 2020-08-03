#  Faça um Programa que peça as 4 notas bimestrais e mostre a média.
def nota_media(nota_1=0.0, nota_2=0.0, nota_3=0.0, nota_4=0.0):
    total = (nota_1 + nota_2 + nota_3 + nota_4) / 4
    return f'Sua nota foi de {int(total)}'


class CalcularMedia:

    def __init__(self, bimestre1=0.0, bimestre2=0.0, bimestre3=0.0, bimestre4=0.0, notatotal=0.0):
        self.bimestre1 = bimestre1
        self.bimestre2 = bimestre2
        self.bimestre3 = bimestre3
        self.bimestre4 = bimestre4
        self.notatotal = notatotal

    def juntar_e_dividir(self):
        self.notatotal = self.bimestre1 + self.bimestre2 + self.bimestre3 + self.bimestre4
        total = self.notatotal / 4
        return f'Sua nota foi de {int(total)}'


if __name__ == '__main__':
    print(nota_media(7.4, 5.9, 7.4, 9.3))
    resultado2 = CalcularMedia(bimestre1=7.0, bimestre2=9.1, bimestre3=10.0, bimestre4=8.5)
    print(resultado2.juntar_e_dividir())

nota1 = int(input('Insira a primeira nota:'))  # resposta certa, corrigido da internet
nota2 = int(input('Insira a segunda nota:'))
nota3 = int(input('Insira a terceira nota:'))
nota4 = int(input('Insira a quarta nota:'))

media = (nota1 + nota2 + nota3 + nota4) / 4

print('A média desse aluno é', media)
