#Refaça o Ex_035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#-Equilátero: todos os lados iguais
#-Isósceles: dois lados iguais
#-Escaleno: todos os lados diferentes

print(f'\n{'- Me informe 3 lados, e eu te digo se é possivel formar um triângulo, e se ele é Equilátero, Isósceles ou Escaleno -':^121}\n')

primeiroLado = int(input('Qual o tamanho do 1º Lado? '))
segundoLado = int(input('Qual o tamanho do 2º Lado? '))
terceiroLado = int(input('Qual o tamanho do 3º Lado? '))

print(f'\nAs medidas {primeiroLado}, {segundoLado} e {terceiroLado}', end=' ')

if primeiroLado + segundoLado > terceiroLado and segundoLado + terceiroLado > primeiroLado and terceiroLado + primeiroLado > segundoLado:
    print('podem forma um Triângulo', end=' ')

    if primeiroLado == segundoLado and segundoLado == terceiroLado:
        print('EQUILÁTERO.\n')
    
    elif primeiroLado == segundoLado or segundoLado == terceiroLado or terceiroLado == primeiroLado:
        print('ISÓSCELES.\n')
    
    else:
        print('ESCALENO.\n')

else:
    print('não podem forma um Triângulo.\n')