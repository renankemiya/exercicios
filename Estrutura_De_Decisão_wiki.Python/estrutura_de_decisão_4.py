letra = input('Insira uma letra: ')
vogais = list('a' 'e' 'i' 'o' 'u')
consoantes = list('b' 'c' 'd' 'f' 'g' 'h' 'j' 'k' 'l' 'm' 'n' 'p' 'q' 'r' 's' 't' 'v' 'w' 'x' 'y' 'z')
for vogal in vogais:
    if vogal == letra:
        print('Essa letra é uma vogal')

for consoante in consoantes:
    if consoante == letra:
        print('Essa letra é uma consoante')
