class RendaPescador:
    def __init__(self, peso):
        self.peso = peso

    def guardar_excesso(self):
        if self.peso > 50:
            excesso = self.peso - 50
            return f'O peso do peixe é de {self.peso} Kg, com o excesso de {excesso} Kg'

    def calcular_renda(self):
        peso = self.peso
        if peso > 50:
            multa = (self.peso - 50) * 4.00
            return f'{self.guardar_excesso()}, A multa é de {multa} Reais'
        else:
            return f'{peso, logo não há multa'



if __name__ == '__main__':
    renda = RendaPescador(52.5)
    print(renda.calcular_renda())

