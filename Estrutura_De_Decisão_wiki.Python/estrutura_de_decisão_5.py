#  Faça um programa para a leitura de duas notas parciais de um aluno.
#  O programa deve calcular a média alcançada por aluno e apresentar:
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez.

nota_1 = float(input('Insira a nota: '))
nota_2 = float(input('Insira outro número: '))
media = (nota_1 + nota_2) / 2

if media == 10:
    print('Aprovado com Distinção')
elif media >= 7:
    print('Aprovado')
elif media < 7:
    print('Reprovado')

#  Correção da internet

nota1 = input("digite sua primeira nota ---> ")
nota2 = input("digite sua segunda nota ---> ")
media = (float(nota1) + float(nota2)) / 2
if media >= 7.0:
    if media == 10.0:
        print("Aprovado con distincao!")
    else:
        print("Aprovado")
else:
    print("Reprovado")
