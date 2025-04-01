from os import system

def obterTemperaturaCelsiusUser():
    temperatura_celsius_user = round(float(input("Digite uma temperatura em °C: ")), 1)
    return temperatura_celsius_user


def transformarCelsiusEmFahrenheit(temperatura_celsius):
    temperatura_fahrenheit = round(((temperatura_celsius * 1.8) + 32), 1)
    return temperatura_fahrenheit


def mostrarResultado(temperatura_celsius, temperatura_fahrenheit):
    print(f"\nA temperatura de {temperatura_celsius}°C, em Fahrenheit é de {temperatura_fahrenheit}°F.\n")


def main():
    system("clear")

    temperatura_em_celsius = obterTemperaturaCelsiusUser()
    temperatura_em_fahrenheit = transformarCelsiusEmFahrenheit(temperatura_em_celsius)

    mostrarResultado(temperatura_em_celsius, temperatura_em_fahrenheit)


main()