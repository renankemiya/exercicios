#  Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda,
#  que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde
#  a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde
#  ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade
#  de horas trabalhadas no mês.
# Desconto do IR:
# Salário Bruto até 900 (inclusive) - isento
# Salário Bruto até 1500 (inclusive) - desconto de 5%
# Salário Bruto até 2500 (inclusive) - desconto de 10%
# Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo.
# No exemplo o valor da hora é 5 e a quantidade de hora é 220.
#         Salário Bruto: (5 * 220)        : R$ 1100,00
#         (-) IR (5%)                     : R$   55,00
#         (-) INSS ( 10%)                 : R$  110,00
#         FGTS (11%)                      : R$  121,00
#         Total de descontos              : R$  165,00
#         Salário Liquido                 : R$  935,00

valor_por_hora = float(input('Insira seu ganho por hora: '))
horas_por_mes = int(input('Insira quantas horas trabalha por mês: '))
salario_bruto = valor_por_hora * horas_por_mes

if salario_bruto <= 900.00:
    sindicato = salario_bruto * 0.03
    fgts = salario_bruto * 0.11
    salario_liquido = salario_bruto - sindicato
    print(f'Salário bruto: ({valor_por_hora}*{horas_por_mes}) : R$ {salario_bruto}')
    print(f'(-) Sindicato (3%)                                : R$ {sindicato}')
    print(f'FGTS (11%)                                        : R$ {fgts}')
    print(f'Total de descontos                                : R$ {sindicato}')
    print(f'Salário Liquido                                   : R$ {salario_liquido}')
elif 900.00 < salario_bruto <= 1500.00:
    imposto_de_renda = salario_bruto * 0.05
    sindicato = salario_bruto * 0.03
    fgts = salario_bruto * 0.11
    salario_liquido = salario_bruto - (sindicato + imposto_de_renda)
    print(f'Salário bruto: ({valor_por_hora}*{horas_por_mes}) : R$ {salario_bruto}')
    print(f'(-) IR (5%)                                       : R$ {imposto_de_renda}')
    print(f'(-) Sindicato (3%)                                : R$ {sindicato}')
    print(f'FGTS (11%)                                        : R$ {fgts}')
    print(f'Total de descontos                                : R$ {sindicato + imposto_de_renda}')
    print(f'Salário Liquido                                   : R$ {salario_liquido}')
elif 1500.00 < salario_bruto <= 2500.00:
    imposto_de_renda = salario_bruto * 0.1
    sindicato = salario_bruto * 0.03
    fgts = salario_bruto * 0.11
    salario_liquido = salario_bruto - (sindicato + imposto_de_renda)
    print(f'Salário bruto: ({valor_por_hora}*{horas_por_mes}) : R$ {salario_bruto}')
    print(f'(-) IR (10%)                                      : R$ {imposto_de_renda}')
    print(f'(-) Sindicato (3%)                                : R$ {sindicato}')
    print(f'FGTS (11%)                                        : R$ {fgts}')
    print(f'Total de descontos                                : R$ {sindicato + imposto_de_renda}')
    print(f'Salário Liquido                                   : R$ {salario_liquido}')
elif salario_bruto > 2500.00:
    imposto_de_renda = salario_bruto * 0.2
    sindicato = salario_bruto * 0.03
    fgts = salario_bruto * 0.11
    salario_liquido = salario_bruto - (sindicato + imposto_de_renda)
    print(f'Salário bruto: ({valor_por_hora}*{horas_por_mes}) : R$ {salario_bruto}')
    print(f'(-) IR (20%)                                      : R$ {imposto_de_renda}')
    print(f'(-) Sindicato (3%)                                : R$ {sindicato}')
    print(f'FGTS (11%)                                        : R$ {fgts}')
    print(f'Total de descontos                                : R$ {sindicato + imposto_de_renda}')
    print(f'Salário Liquido                                   : R$ {salario_liquido}')

#  Correção da internet
taxaIrList = [0.0, 0.05, 0.1, 0.2]
horasTrabalho = float(input("digite a quantidade de horas trabalhadas ---> "))
valorHora = float(input("digite o valor em reais da sua hora de trabalho ---> "))
salarioBruto = horasTrabalho * valorHora
taxaInss = 0.1
fgts = 0.11
if salarioBruto <= 900:
    taxaIr = taxaIrList[0]
if 900 < salarioBruto <= 1500:
    taxaIr = taxaIrList[1]
if 1500 < salarioBruto <= 2500:
    taxaIr = taxaIrList[2]
if salarioBruto > 2500:
    taxaIr = taxaIrList[3]
descontos = (salarioBruto * taxaIr) + (salarioBruto * taxaInss)
print("Salario Bruto: (", valorHora, " * ", horasTrabalho, ") ----> R$ ", salarioBruto)
print("(-) IR (", taxaIr * 100, "%) ----> R$ ", salarioBruto * taxaIr)
print("(-) INSS (", taxaInss * 100, "%) ----> R$ ", salarioBruto * taxaInss)
print("FGTS (11%) ----> R$ ", salarioBruto * fgts)
print("Salario Liquido R$ ----> ", salarioBruto - descontos)
