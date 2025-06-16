#Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo 
#e usa algumas dessas funções.

import moeda

número = int(input('\nMe informe um número: '))

print()

moeda.aumentar(número)
moeda.diminuir(número)
moeda.dobro(número)
moeda.metade(número)

print()