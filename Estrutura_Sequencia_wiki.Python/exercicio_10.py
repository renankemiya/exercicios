class TemperaturaCelsius:
    def __init__(self, celsius):
        self.celsius = celsius

    def converter_celsius_farenheit(self):
        farenheit = self.celsius / 5
        farenheit = (farenheit * 9) + 32
        return f'Graus Farenheit: {farenheit}'

def converter_teperatura(celsius):
    farenheit = celsius / 5
    farenheit = (farenheit * 9) + 32
    return f'Graus Farenheit: {farenheit}'

if __name__ == '__main__':
    farenheit = TemperaturaCelsius(100)
    print(farenheit.converter_celsius_farenheit())
    print(converter_teperatura(300))