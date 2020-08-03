#  Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área
#  a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é
#  vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta
#  a serem compradas e o preço total.


class CalculadorDeTinta:
    def __init__(self, area_c):
        self.area_c = area_c  # metros quadrados
        self.lata_volume = 18  # litros
        self.preco = 80.00  # reais

    def cobertura_por_litro(self):
        lata = 0
        litros_de_tinta = self.area_c / 3
        unidade_lata = litros_de_tinta / 18
        while unidade_lata > 0:
            lata += 1
            unidade_lata -= 1
        custo = lata * self.preco
        return f'Em {self.area_c} metros quadrados são necessarias {lata} latas de tinta, com o preço de {custo} Reais'


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

area = float(input('Qual a area a ser pintada? (em metros quadrados): '))  # resposta certa, corrigido da internet
quantidade_de_latas = area // 54  # uma lata pinta 54 metros quadrados

if area % 54 != 0:
    quantidade_de_latas += 1

preco = quantidade_de_latas * 80

print('A quantidade de latas a serem compradas é', quantidade_de_latas)
print('e o valor a ser pago será', preco)
