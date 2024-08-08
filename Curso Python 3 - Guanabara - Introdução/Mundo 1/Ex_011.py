#Faça um programa que leia a largara e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta nescessária para pintá-la, sabendo que cada 
# litro de tinta pinta uma área de 2m².

print(f'\n{'- Informe a largura e altura de sua parede, e eu te informo a quantidade de tinta necessária para pintá-la -':^113}\n')

larguraDaParede = float(input('Qual a Largura(em metros)? '))

alturaDaParede = float(input('Qual a Altura(em metros)? '))

áreaDaParede = larguraDaParede * alturaDaParede
quantidadeDeTinta = áreaDaParede / 2

print(f'\nA sua parede possui uma área de {áreaDaParede:.2f}m², logo irá precisar de {quantidadeDeTinta:.1f}L de tinta para pintá-la por completo.\n')