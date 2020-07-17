class TemperaturaFarenheit:
    def __init__(self, farenheit):
        self.farenheit = farenheit

    def converter_farenheit_celsius(self):
        celsius = self.farenheit - 32
        celsius = (celsius / 9) * 5
        return f'Graus Celsius: {celsius}'


def converter_teperatura(farenheit):
    celsius = farenheit - 32
    celsius = (celsius / 9) * 5
    return f'Graus Celsius: {celsius}'


if __name__ == '__main__':
    temperatura = TemperaturaFarenheit(122)
    print(temperatura.converter_farenheit_celsius())
    print(converter_teperatura(410))
