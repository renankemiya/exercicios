def somar(parametro, parametro_2):
    return parametro + parametro_2


class Calcular:

    def __init__(self, numero_1=0, numero_2=0):
        self.numero_1 = numero_1
        self.numero_2 = numero_2

    def juntar(self):
        numero_s = self.numero_1 + self.numero_2
        return numero_s


if __name__ == '__main__':
    print(somar(1, 3))
    resultado = Calcular()
    resultado.numero_1 = 5430
    resultado.numero_2 = 300
    print(resultado.numero_1)
    print(resultado.numero_2)
    print(resultado.juntar())

x = int(input('Insira um número: '))  # resposta certa, corrigido da internet
y = int(input('Insira outro número: '))

print('A soma desses números é:', x+y)
