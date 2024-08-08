#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vaai custar R$7.00 por cada Km acima do limite.

print(f'\n{'- Me informe a velocidade do carro, e eu te digo se foi acima ou abaixo da velicidade máxima da pista -':^108}\n')

velocidadeDoCarro = int(input('Qual a sua velocidade? '))

if velocidadeDoCarro <= 80:
    print('\nVOCÊ ESTÁ DENTRO DO LIMITE DE 80KM/H!\nSiga com segunça e use SEMPRE o Cinto\n')
else:
    print(f'\nVOCÊ FOI MULTADO! ULTRAPASSOU O LIMITE DE 80KM/H!\n{f'O valor da multa ficou em R${(velocidadeDoCarro-80)*7:.2f}.':^49}\n')