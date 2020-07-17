class Temperatura:
    def __init__(self, farenheit):
        self.farenheit = farenheit

    def converter_farenheit_celsius(self):
        celsius = self.farenheit - 32
        celsius = (celsius / 9) * 5
        return celsius, 'Graus Celsius'


def converter_teperatura(farenheit):
    celsius = farenheit - 32
    celsius = (celsius / 9) * 5
    return celsius, 'Graus Celsius'


if __name__ == '__main__':
    temperatura = Temperatura(122)
    print(temperatura.converter_farenheit_celsius())
    print(converter_teperatura(410))
