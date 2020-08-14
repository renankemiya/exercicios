#  Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade
#  de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download
#  do arquivo usando este link (em minutos).


class CalculadorDeVelocidade:
    def __init__(self, tamanho, velocidade):
        self.velocidade = velocidade  # em Mbps
        self.tamanho = tamanho  # em MB

    def calculador(self):
        segundo = 0
        em_bytes = self.tamanho * 1_048_576
        v_em_bytes = self.velocidade * 1_048_576
        while em_bytes > 0:
            segundo += 1
            em_bytes -= v_em_bytes
        minuto = int(segundo / 60)
        return f'Aproximadamente {minuto} minutos para baixar por esse link'


if __name__ == '__main__':
    medidor = CalculadorDeVelocidade(500, 1.72)
    print(medidor.calculador())

arquivo = float(input('Qual o tamanho do arquivo em MB?: '))  # resposta certa, corrigido da internet
link = float(input('Qual a velocidade do link de internet em Mbps? '))

tempo = (arquivo / link)
tempo_min = tempo // 60
tempo_seg = tempo - tempo_min

print(f'O tempo aproximado de download é de {tempo_min} minutos e {tempo_seg} segundos')
