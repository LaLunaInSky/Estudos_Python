#Escreva um programa que converta uma temperatura digitada em °C e para °F. (Celsius para Fahrenheit)

print(f'\n{'- Me informe uma temperatura em Celsius e eu te retorno a mesma em Fahrenheit -':^84}\n')

temperaturaEmCelsius = float(input('Qual a temperatura(Celsius/°C)? '))

temperaturaEmFarenheit = temperaturaEmCelsius * 1.8 + 32 

print(f'\nA temperatura informada de {temperaturaEmCelsius}°C em Fahrenheit é igual a {temperaturaEmFarenheit}°F.\n')