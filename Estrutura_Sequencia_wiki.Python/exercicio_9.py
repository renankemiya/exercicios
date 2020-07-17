class Temperatura:
    def __init__(self, farenheit):
        self.farenheit = farenheit

    def converter_farenheit_celsius(self):
        celsius = self.farenheit - 32
        celsius = (celsius / 9) * 5
        return celsius

if __name__ == '__main__':
