class CalculadorDeTinta:
    def __init__(self, area):
        self.area = area  # metros quadrados
        self.lata_volume = 18  # litros
        self.galoes_volume = 3.6  # litros
        self.preco_lata = 80.00  # reais
        self.preco_galao = 25.00  # reais

    def apenas_latas(self):
        lata = 0
        litros_de_tinta = self.area / 6
        unidade_lata = litros_de_tinta / 18
        while unidade_lata > 0:
            lata += 1
            unidade_lata -= 1
        custo = lata * self.preco_lata
        return f'Em {self.area} metros quadrados são necessárias {lata} latas de tinta, com o preço de {custo} reais'

    def apenas_galoes(self):
        galao = 0
        litros_de_tinta = self.area / 6
        unidade_galao = litros_de_tinta / 3.6
        while unidade_galao > 0:
            galao += 1
            unidade_galao -= 1
        custo = galao * self.preco_galao
        return f'Em {self.area} metros quadrados são necessários {galao} galões de tinta, com o preço de {custo} reais'

    def latas_e_galoes(self):
        lata = 0
        galao = 0
        litros_de_tinta = self.area / 6
        while litros_de_tinta >= 18:
            lata += 1
            litros_de_tinta -= 18
        unidade_galao = litros_de_tinta / 3.6
        while unidade_galao > 0:
            galao += 1
            unidade_galao -= 1
        custo = (lata * self.preco_lata) + (galao * self.preco_galao)
        return f'Em {self.area} metros quadrados são necessárias {lata} latas de tinta e {galao} galões de tinta, com' \
               f' o preço de {custo} reais'


if __name__ == '__main__':
    cliente = CalculadorDeTinta(5300)
    print(cliente.apenas_latas())
    print(cliente.apenas_galoes())
    print(cliente.latas_e_galoes())