#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

print(f'\n{'- Me informe 6 números inteiros, e eu somo os que forem pares -':^68}\n')

somaDosNúmerosPares = 0

for contagem in range(1, 7):
    númeroInformado = int(input(f'Qual o {contagem}º número? '))

    if númeroInformado % 2 == 0:
        somaDosNúmerosPares += númeroInformado

print(f'\nA soma dos números pares informados foi de {somaDosNúmerosPares}.\n')