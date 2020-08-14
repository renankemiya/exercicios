#  As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver
#  o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo
# o seguinte critério, baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.

salario = float(input('Insira seu Salário: '))

if salario <= 280.00:
    antes_do_reajuste = salario
    percentual_aplicado = '20%'
    aumentar_salario = salario * 0.2
    salario_novo = salario + aumentar_salario
    print(f'Salário antes do reajuste: {antes_do_reajuste} reais, '
          f'Percentual aplicado: {percentual_aplicado}, '
          f'Valor aumentado: {aumentar_salario} reais, '
          f'Novo salário: {salario_novo} reais')
elif 280.00 < salario <= 700.00:
    antes_do_reajuste = salario
    percentual_aplicado = '15%'
    aumentar_salario = salario * 0.15
    salario_novo = salario + aumentar_salario
    print(f'Salário antes do reajuste: {antes_do_reajuste} reais, '
          f'Percentual aplicado: {percentual_aplicado}, '
          f'Valor aumentado: {aumentar_salario} reais, '
          f'Novo salário: {salario_novo} reais')
elif 700.00 < salario < 1500.00:
    antes_do_reajuste = salario
    percentual_aplicado = '10%'
    aumentar_salario = salario * 0.1
    salario_novo = salario + aumentar_salario
    print(f'Salário antes do reajuste: {antes_do_reajuste} reais, '
          f'Percentual aplicado: {percentual_aplicado}, '
          f'Valor aumentado: {aumentar_salario} reais, '
          f'Novo salário: {salario_novo} reais')
elif salario >= 1500.00:
    antes_do_reajuste = salario
    percentual_aplicado = '5%'
    aumentar_salario = salario * 0.05
    salario_novo = salario + aumentar_salario
    print(f'Salário antes do reajuste: {antes_do_reajuste} reais, '
          f'Percentual aplicado: {percentual_aplicado}, '
          f'Valor aumentado: {aumentar_salario} reais, '
          f'Novo salário: {salario_novo} reais')

#  Correção da internet
salarioAjustado = 0
aumentoPer = 0
aumentoVal = 0
salario = float(input("digite seu salario ---> "))
if salario <= 280:
    aumentoPer = 0.2
    aumentoVal = aumentoPer * salario
    salarioAjustado = salario * (1 + aumentoPer)
if 280 < salario <= 700:
    aumentoPer = 0.15
    aumentoVal = aumentoPer * salario
    salarioAjustado = salario * (1 + aumentoPer)
if 700 < salario <= 1500:
    aumentoPer = 0.1
    aumentoVal = aumentoPer * salario
    salarioAjustado = salario * (1 + aumentoPer)
if 1500 < salario:
    aumentoPer = 0.05
    aumentoVal = aumentoPer * salario
    salarioAjustado = salario * (1 + aumentoPer)
print("salario - R$ ", salario)
print("percentual de aumnento aplicado - ", aumentoPer * 100, "%")
print("valor do aumento - R$ ", aumentoVal)
print("salario ajustado - R$ ", salarioAjustado)
