#  Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = input('Insira uma letra: ')
vogais = list('a' 'e' 'i' 'o' 'u')
consoantes = list('b' 'c' 'd' 'f' 'g' 'h' 'j' 'k' 'l' 'm' 'n' 'p' 'q' 'r' 's' 't' 'v' 'w' 'x' 'y' 'z')
for vogal in vogais:
    if letra == vogal:
        print('Essa letra é uma vogal')

for consoante in consoantes:
    if letra == consoante:
        print('Essa letra é uma consoante')

#  Correção da internet

letra = input("digite uma letra (ex: \"a\") : ")
if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
    print(letra, "eh uma vogal")
else:
    print(letra, "eh uma consoante")
