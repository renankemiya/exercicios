class Conversor:
    def __init__(self, metro):
        self.metro = metro

    def conversor(self):
        return self.metro * 100


if __name__ == '__main__':
    valor = Conversor(1)
    print(valor.conversor())
    valor.metro = 10
    print(valor.conversor())
