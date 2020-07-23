salario = float(input('Insira seu Salário: '))

if salario <= 280.00:
    antes_do_reajuste = salario
    percentual_aplicado = '20%'
    aumentar_salario = salario * 0.2
    salario_novo = salario + aumentar_salario
    print(f'Salário antes do reajuste: {antes_do_reajuste}, '
          f'Percentual aplicado: {percentual_aplicado}, '
          f'Valor aumentado: {aumentar_salario}, '
          f'Novo salário: {salario_novo}')
elif 280.00 < salario <= 700.00:
    antes_do_reajuste = salario
    percentual_aplicado = '15%'
    aumentar_salario = salario * 0.15
    salario_novo = salario + aumentar_salario
    print(f'Salário antes do reajuste: {antes_do_reajuste}, '
          f'Percentual aplicado: {percentual_aplicado}, '
          f'Valor aumentado: {aumentar_salario}, '
          f'Novo salário: {salario_novo}')
elif 700.00 < salario < 1500.00:
    antes_do_reajuste = salario
    percentual_aplicado = '10%'
    aumentar_salario = salario * 0.1
    salario_novo = salario + aumentar_salario
    print(f'Salário antes do reajuste: {antes_do_reajuste}, '
          f'Percentual aplicado: {percentual_aplicado}, '
          f'Valor aumentado: {aumentar_salario}, '
          f'Novo salário: {salario_novo}')
elif salario >= 1500.00:
    antes_do_reajuste = salario
    percentual_aplicado = '5%'
    aumentar_salario = salario * 0.05
    salario_novo = salario + aumentar_salario
    print(f'Salário antes do reajuste: {antes_do_reajuste}, '
          f'Percentual aplicado: {percentual_aplicado}, '
          f'Valor aumentado: {aumentar_salario}, '
          f'Novo salário: {salario_novo}')
