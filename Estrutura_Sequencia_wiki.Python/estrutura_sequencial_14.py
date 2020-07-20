class RendaPescador:
    def __init__(self, peso):
        self.peso = peso

    def calcular_renda(self):
        if self.peso > 50:
            excesso = self.peso - 50
            multa = excesso * 4.00
            return f'O peso do peixe é de {self.peso} Kg, ' \
                   f'com o excesso de {excesso}, A multa é de {multa} Reais'
        else:
            return f'O peso do peixe é de {self.peso} Kg, logo não há multa'


if __name__ == '__main__':
    renda = RendaPescador(52.5)
    print(renda.calcular_renda())
    renda = RendaPescador(34)
    print(renda.calcular_renda())
