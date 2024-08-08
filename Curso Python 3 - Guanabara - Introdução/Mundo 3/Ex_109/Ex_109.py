#Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo 
#e usa algumas dessas funções. Modifque as funções criadas para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não 
#formatado pela função moeda().

import moedas

preçoInformado = float(input('\nQual o preço? R$'))

print(f'''
O preço de {moedas.moeda(preçoInformado)}:
→ O dobro é {moedas.dobro(preçoInformado, mostrarMoeda=True)}
→ A metade é {moedas.metade(preçoInformado, mostrarMoeda=True)}
→ Com o aumento de 25% é {moedas.aumentar(preçoInformado, 25, mostrarMoeda=True)}
→ Com o desconto de 5% é {moedas.diminuir(preçoInformado, 5, mostrarMoeda=True)}
''')