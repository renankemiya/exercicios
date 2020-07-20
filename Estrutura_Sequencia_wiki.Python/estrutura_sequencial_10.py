class TemperaturaCelsius:
    def __init__(self, celsius):
        self.celsius = celsius

    def converter_celsius_farenheit(self):
        farenheit_c = self.celsius / 5
        farenheit_c = (farenheit_c * 9) + 32
        return f'Graus Farenheit: {farenheit_c}'


def converter_teperatura(celsius):
    farenheit_f = celsius / 5
    farenheit_f = (farenheit_f * 9) + 32
    return f'Graus Farenheit: {farenheit_f}'


if __name__ == '__main__':
    farenheit = TemperaturaCelsius(100)
    print(farenheit.converter_celsius_farenheit())
    print(converter_teperatura(300))

C = float(input('Informe a temperatura em Celsius: '))  # resposta certa, corrigido da internet

F = 9 * C / 5 + 32

print('Graus Farenheit: ', F)
