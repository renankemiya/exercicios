class CalculadorDeTinta:
    def __init__(self, area):
        self.area = area # metros quadrados
        self.lata_volume = 18 # litros
        self.preco = 80.00 # reais

    def cobertura_por_litro(self):
        lata = 0
        litros_de_tinta = self.area / 3
        unidade_lata = litros_de_tinta / 18
        while unidade_lata > 0:
            lata += 1
            unidade_lata -= 1
        custo = lata * self.preco
        return f'Em {self.area} metros quadrados são necessarias {lata} latas de tinta, com o preço de {custo} Reais'



if __name__ == '__main__':
    comprador = CalculadorDeTinta(120)
    print(comprador.cobertura_por_litro())
    comprador = CalculadorDeTinta(26)
    print(comprador.cobertura_por_litro())
    comprador = CalculadorDeTinta(9)
    print(comprador.cobertura_por_litro())
    comprador = CalculadorDeTinta(580)
    print(comprador.cobertura_por_litro())
    comprador = CalculadorDeTinta(70)
    print(comprador.cobertura_por_litro())
