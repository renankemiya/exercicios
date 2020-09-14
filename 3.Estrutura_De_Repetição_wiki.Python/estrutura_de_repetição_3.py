#  Faça um programa que leia e valide as seguintes informações:
#  a. Nome: maior que 3 caracteres;
#  b. Idade: entre 0 e 150;
#  c. Salário: maior que zero;
#  d. Sexo: 'f' ou 'm';
#  e. Estado Civil: 's', 'c', 'v', 'd';

nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
salario = float(input('Digite seu salário: '))
sexo = input('Digite seu sexo f para Feminino e m para Masculino: ')
estado_civil = input('Digite seu estado civil, s para solteiro, c para casado, v para viuvo e d para divorciado: ')

while len(nome) <= 3:
    print('O nome precisa ter mais de 3 caracteres')
    nome = input('Digite seu nome: ')
while idade < 0 or idade > 150:
    print('A idade não pode ser menor que 0 ou maior que 150')
    idade = int(input('Digite sua idade: '))
while salario <= 0:
    print('O salário deve ser maior que 0')
    salario = float(input('Digite seu salário: '))
while (sexo != 'f') and (sexo != 'm'):
    print('Sexo inválido, tente novamente')
    sexo = input('Digite seu f para Feminino e m para Masculino: ')
while (estado_civil != 's') and (estado_civil != 'c') and (estado_civil != 'v') and (estado_civil != 'd'):
    print('Opção inválida, tente novamente')
    estado_civil = input('Digite seu estado civil, s para solteiro, c para casado, v para viuvo e d para divorciado: ')

print('Nome:', nome)
print('Idade:', idade)
print('Salário:', salario)
print('Sexo:', sexo)
print('Estado Civil:', estado_civil)
