class CalculadorDeTinta:
    def __init__(self, area):
        self.area = area  # metros quadrados
        self.lata_volume = 18  # litros
        self.galoes_volume = 3.6  # litros
        self.preco_lata = 80.00  # reais
        self.preco_galao = 25.00  # reais
        self.margem = int(self.area * 1.1)  # margem de 10%

    def apenas_latas(self):
        lata = 0
        litros_de_tinta = self.margem / 6
        unidade_lata = litros_de_tinta / 18
        while unidade_lata > 0:
            lata += 1
            unidade_lata -= 1
        custo = lata * self.preco_lata
        return f'Em {self.margem} metros quadrados são necessárias {lata} latas de tinta, com o preço de {custo} reais'

    def apenas_galoes(self):
        galao = 0
        litros_de_tinta = self.margem / 6
        unidade_galao = litros_de_tinta / 3.6
        while unidade_galao > 0:
            galao += 1
            unidade_galao -= 1
        custo = galao * self.preco_galao
        return f'Em {self.margem} metros quadrados são necessários {galao} galões de tinta,' \
               f' com o preço de {custo} reais'

    def latas_e_galoes(self):
        lata = 0
        galao = 0
        litros_de_tinta = self.margem / 6
        while litros_de_tinta >= 18:
            lata += 1
            litros_de_tinta -= 18
        unidade_galao = litros_de_tinta / 3.6
        while unidade_galao > 0:
            galao += 1
            unidade_galao -= 1
        custo = (lata * self.preco_lata) + (galao * self.preco_galao)
        return f'Em {self.margem} metros quadrados são necessárias {lata} latas de tinta e {galao} ' \
               f'galões de tinta, com o preço de {custo} reais '


if __name__ == '__main__':
    cliente = CalculadorDeTinta(2640)
    print(cliente.apenas_latas())
    print(cliente.apenas_galoes())
    print(cliente.latas_e_galoes())

metro = float(input('Qual a area a ser pintada? (em metros quadrados) '))  # resposta certa, corrigido da internet
margem = metro * 1.1
print('Metragem com margem de 10%: ', int(margem), 'm²')

quantidade_de_latas = margem // 108
quantidade_de_galoes = margem // 21.6

if margem % 108 > 0:  # primeira situação
    quantidade_de_latas += 1
preco_lata = quantidade_de_latas * 80
print(f'Se comprar somente latas, o preço será {preco_lata} reais comprando {quantidade_de_latas} latas')

if margem % 21.6 > 0:  # segunda situação
    quantidade_de_galoes += 1
preco_galao = quantidade_de_galoes * 25
print(f'Se comprar somente galões, o preço será {preco_galao} reais comprando {quantidade_de_galoes} galões')

if margem % 108 > 0:  # terceira situação
    quantidade_de_latas = margem // 108
    sobra = (margem / 108 - margem // 108) * 108
    quantidade_de_galoes = sobra // 21.6
    if sobra % 21.6 > 0:
        quantidade_de_galoes += 1

preco_lata_2 = quantidade_de_latas * 80
preco_galao_2 = quantidade_de_galoes * 25
preco_total = preco_lata_2 + preco_galao_2
print(f'A quantidade de latas é {quantidade_de_latas} e a quantidade de galões é {quantidade_de_galoes},'
      f' o preço total é de {preco_total}')
