#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import radians, sin, cos, tan

print(f'\n{'- Informe um ângulo qualquer, e eu te digo o seu seno, cosseno e sua tangente -':^84}\n')

ânguloInformado = float(input('Qual o ângulo? '))

radianoDoÂngulo = radians(ânguloInformado)

print(f'\nO ângulo informado foi {ânguloInformado}°, o seu Seno é de {sin(radianoDoÂngulo):.2f}, Cosseno é {cos(radianoDoÂngulo):.2f}, e Tangente é {tan(radianoDoÂngulo):.2f}\n')