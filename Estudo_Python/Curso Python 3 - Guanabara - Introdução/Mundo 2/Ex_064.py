#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
#No final mostre quantos números foram digitados, e qual foi a soma entre eles (desconsiderando o flag).

print(f'\n{'- Me informe vários números inteiros, e eu irei somar todos eles -':^71}\n')

númeroInformado = 0
númerosInformados = []

while númeroInformado != 999:
    númeroInformado= int(input('Qual número você quer(999 para encerrar)? '))
    
    if númeroInformado != 999:
        númerosInformados.append(númeroInformado)

somaDosNúmeros = 0

for contagem in range(0, len(númerosInformados)):
    somaDosNúmeros += númerosInformados[contagem]

print(f'\nForam digitados {len(númerosInformados)} números, a soma de tudo é {somaDosNúmeros}.\n')