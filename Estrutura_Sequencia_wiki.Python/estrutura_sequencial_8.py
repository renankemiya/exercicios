class SalarioMensal:
    meses = {'Janeiro': 31, 'Fevereiro': 29, 'Março': 31, 'Abril': 30, 'Maio': 31, 'Junho': 30,
             'Julho': 31, 'Agosto': 31, 'Setembro': 30, 'Outubro': 31, 'Novembro': 30, 'Dezembro': 31}

    def __init__(self, valor_por_hora, horas_por_dia, mes):
        self.mes = mes
        self.horas_por_dia = horas_por_dia
        self.valor_por_hora = valor_por_hora
        self.horas_por_mes = self.horas_por_dia * self.meses[self.mes]

    def calcular_salario(self):
        salario_calculado = self.valor_por_hora * self.horas_por_mes
        return f'{self.mes}: {salario_calculado}'


def salario_mensal(valor, horas, mes):
    meses = {'Janeiro': 31, 'Fevereiro': 29, 'Março': 31, 'Abril': 30, 'Maio': 31, 'Junho': 30,
             'Julho': 31, 'Agosto': 31, 'Setembro': 30, 'Outubro': 31, 'Novembro': 30, 'Dezembro': 31}
    resultado = valor * horas * meses[mes]
    return f'{mes}: {resultado}'


if __name__ == '__main__':
    salario_c = SalarioMensal(30.43, 10, 'Janeiro')
    print(salario_c.calcular_salario())
    print(salario_mensal(72, 7, 'Agosto'))

hora = float(input('Quanto você ganhar por hora?: '))  # resposta certa, corrigido da internet
tempo = float(input('Quantas horas você trabalha por mês?: '))

salario = hora * tempo

print('Seu salário é de: ', salario, ' reais')
