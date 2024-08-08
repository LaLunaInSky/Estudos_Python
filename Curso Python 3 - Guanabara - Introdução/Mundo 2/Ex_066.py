#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
#No final, mostre quantos números foram digitados e qual foi a soma entre eles (Desconsiderando o flag).

print(f'\n{'- Me informe números qualquer, e eu te devolvo a soma deles e quantos foram digitados -':^92}\n')

somaDosNúmerosInformados = contadorDeVezes = 0

while True:
    númeroInformado = int(input('Digite um número(999 para encerrar!): '))

    if númeroInformado == 999:
        break
    
    contadorDeVezes += 1
    somaDosNúmerosInformados += númeroInformado

print(f'\nForam digitados {contadorDeVezes} números, a soma deles é igual à {somaDosNúmerosInformados}.\n')