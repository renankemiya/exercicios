#  Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
#  Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
#  8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#  a. salário bruto.
#  b. quanto pagou ao INSS.
#  c. quanto pagou ao sindicato.
#  d. o salário líquido.
#  e. calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$
# Obs.: Salário Bruto - Descontos = Salário Líquido.


class Salario:
    meses = {'Janeiro': 31, 'Fevereiro': 29, 'Março': 31, 'Abril': 30, 'Maio': 31, 'Junho': 30,
             'Julho': 31, 'Agosto': 31, 'Setembro': 30, 'Outubro': 31, 'Novembro': 30, 'Dezembro': 31}

    def __init__(self, ganho_por_hora, horas_por_dia, mes):
        self.ganho_por_hora = ganho_por_hora
        self.horas_por_dia = horas_por_dia
        self.mes = mes
        self.horas_por_mes = self.horas_por_dia * self.meses[self.mes]
        self.valor_bruto = self.ganho_por_hora * self.horas_por_mes
        self.imposto_de_renda = (self.valor_bruto / 100) * 11
        self.inss = (self.valor_bruto / 100) * 8
        self.sindicato = (self.valor_bruto / 100) * 5

    def calcular_salario(self):
        descontos = self.imposto_de_renda + self.inss + self.sindicato
        valor_liquido = self.valor_bruto - descontos
        return f'a: salário bruto de {self.valor_bruto} Reais', \
               f'b: pago ao INSS o valor de {self.inss} Reais', \
               f'c: pago ao Sindicato o valor de {self.sindicato} Reais', \
               f'd: salário liquido de {valor_liquido} Reais', \
               f'No mês de {self.mes}, pago o Imposto de renda com valor {self.imposto_de_renda}'


if __name__ == '__main__':
    salario = Salario(26, 8, 'Setembro')
    print(salario.valor_bruto)
    print(salario.imposto_de_renda)
    print(salario.inss)
    print(salario.sindicato)
    print(salario.calcular_salario())


hora = float(input('Quanto você ganhar por hora?: '))  # resposta certo, corrigido da internet
tempo = float(input('Quantas horas você trabalha por mês?: '))

salario_bruto = hora * tempo
ir = salario_bruto*0.11
inss = salario_bruto*0.08
sindicato = salario_bruto*0.05
salario_liquido = salario_bruto - ir - inss - sindicato

print('Seu salário bruto é: ', salario_bruto)
print('O valor pago ao INSS é: ', inss)
print('O valor pago ao Sindicato é: ', sindicato)
print('Seu salário liquido será : ', salario_liquido)
