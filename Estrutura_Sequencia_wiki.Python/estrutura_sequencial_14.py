#  João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
#  Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo
#  (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que
#  leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do
#  limite e na variável multa o valor da multa que João deverá pagar.
#  Imprima os dados do programa com as mensagens adequadas.


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
