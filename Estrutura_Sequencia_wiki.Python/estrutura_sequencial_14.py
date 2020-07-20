class RendaPescador:
    def __init__(self, peso_c):
        self.peso_c = peso_c

    def calcular_renda(self):
        if self.peso_c > 50:
            excesso = self.peso_c - 50
            multa_c = excesso * 4.00
            return f'O peso do peixe é de {self.peso_c} Kg, ' \
                   f'com o excesso de {excesso}, A multa é de {multa_c} Reais'
        else:
            return f'O peso do peixe é de {self.peso_c} Kg, logo não há multa'


if __name__ == '__main__':
    renda = RendaPescador(52.5)
    print(renda.calcular_renda())
    renda = RendaPescador(34)
    print(renda.calcular_renda())

peso = float(input('Quantos quilos você pegou hoje?: '))  # resposta certa, corrigido da internet

excedente = peso - 50

if excedente > 0:
    multa = 4 * excedente
else:
    multa = 0
    excedente = 0

print(f'Você pegou {excedente} quilos excedentes, portanto o valor da multa é {multa} reais')
