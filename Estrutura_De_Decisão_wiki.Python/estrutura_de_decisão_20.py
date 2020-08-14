#  Faça um Programa para leitura de três notas parciais de um aluno.
#  O programa deve calcular a média alcançada por aluno e presentar:
# A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
# A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
# A mensagem "Aprovado com Distinção", se a média for igual a 10.

nota_1 = float(input('Insira a primeira nota: '))
nota_2 = float(input('Insira a segunda nota: '))
nota_3 = float(input('Insira a terceira nota: '))
media = (nota_1 + nota_2 + nota_3) / 3

if media == 10:
    print(f'Aprovado com Distinção: {media}')
elif 7 < media < 10:
    print(f'Aprovado: {media}')
elif media < 7:
    print(f'Reprovado: {media}')
