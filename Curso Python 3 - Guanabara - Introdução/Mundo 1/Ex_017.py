#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo, calcule e mostre o comprimento da hipotenusa.

from math import hypot

print(f'\n{'- Me informe o cateto oposto e o adjacente, e eu te informo a hipotenusa -':^79}\n')

catetoOposto = float(input('Qual o cateto Oposto? '))

catetoAdjacente = float(input('Qual o cateto Adjacente? '))

hipotenusaTeoria = (catetoOposto**2 + catetoAdjacente**2) ** (1/2)

hipotenusaMóduloMath = hypot(catetoOposto, catetoAdjacente)

print(f'\nO cateto Oposto {catetoOposto} e o cateto Adjacente {catetoAdjacente} informados, vão ter a Hipotenusa de {hipotenusaTeoria:.2f}. (Teoria Matemática)')

print(f'O cateto Oposto {catetoOposto} e o cateto Adjacente {catetoAdjacente} informados, vão ter a Hipotenusa de {hipotenusaMóduloMath:.2f}. (Módulo Math) \n')