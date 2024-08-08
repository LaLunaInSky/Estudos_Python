#Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

print(f'\n{'- Me informe as dimensões de um terreno, e eu te devolvo a área do mesmo -':^79}\n')

def área(largura, altura):
    a = largura * altura
    print(f'\nO terreno com {largura}cm X {altura}cm tem a área de {a}cm².\n')


área(
    float(input('Qual a largura do terreno? ')),
    float(input('Qual a altura do terreno? '))
)