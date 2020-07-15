def nota_media(nota1=0.0, nota2=0.0, nota3=0.0, nota4=0.0):
    return (nota1 + nota2 + nota3 + nota4) / 4


class NotaMedia:
    def __init__(self, valor1=0.0, valor2=0.0, valor3=0.0, valor4=0.0):
        self.valor1 = valor1
        self.valor3 = valor3
        self.valor2 = valor2
        self.valor4 = valor4

    def somar(self):
        media = self.valor1 + self.valor2 + self.valor3 + self.valor4
        return media / 4


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
    print(nota_media(7.4, 5.9, 5.4, 9.3))
    resultado = NotaMedia()
    resultado.valor1 = 2.3
    resultado.valor2 = 5.4
    resultado.valor3 = 8.7
    resultado.valor4 = 4.9
    print(resultado.somar())
    resultado2 = CalcularMedia()
    resultado2.bimestre1 = 4
    print(resultado2.juntar_e_dividir())
