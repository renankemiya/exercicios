def nota_media(nota1=0.0, nota2=0.0, nota3=0.0, nota4=0.0):
    return (nota1 + nota2 + nota3 + nota4) / 4

class CalcularMedia:

    def __init__(self, bimestre1=0.0, bimestre2=0.0, bimestre3=0.0, bimestre4=0.0, notatotal=0.0):
        self.bimestre1 = bimestre1
        self.bimestre2 = bimestre2
        self.bimestre3 = bimestre3
        self.bimestre4 = bimestre4
        self.notatotal = notatotal

    def juntar_e_dividir(self):
        self.notatotal = self.bimestre1 + self.bimestre2 + self.bimestre3 + self.bimestre4
        return self.notatotal / 4


if __name__ == '__main__':
    print(nota_media(7.4, 5.9, 7.4, 9.3))
    resultado2 = CalcularMedia(bimestre1=7.0, bimestre2=9.1, bimestre3=10.0, bimestre4=8.5)
    print(resultado2.juntar_e_dividir())
