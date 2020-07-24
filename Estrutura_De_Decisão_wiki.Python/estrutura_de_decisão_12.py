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
