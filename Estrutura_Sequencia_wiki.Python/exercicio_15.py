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
               f'd: salário liquido de {valor_liquido} Reais'


if __name__ == '__main__':
    salario = Salario(26,8,'Setembro')
    print(salario.valor_bruto)
    print(salario.imposto_de_renda)
    print(salario.inss)
    print(salario.sindicato)
    print(salario.calcular_salario())