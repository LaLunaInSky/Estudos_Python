#Faça um programa que leia o peso de cinco pessoas, e no final mostre qual foi o maior e o menor dos pesos listados.

print(f'\n{'- Me informe 5 pesos de pessoas, e eu te digo qual foi o amior e o menor deles -':^85}\n')

maiorPeso = 0
menorPeso = 0

for contagem in range(1, 6):
    pesoInformado = float(input(f'Qual o {contagem}º Peso(Kg)? '))
    
    if maiorPeso == 0 and menorPeso == 0:
        maiorPeso = pesoInformado
        menorPeso = pesoInformado
    
    elif pesoInformado < menorPeso:
        menorPeso = pesoInformado

    elif pesoInformado > maiorPeso:
        maiorPeso = pesoInformado

print(f'\nEntre os pesos informados o menor foi de {menorPeso:.1f}Kg e o maior foi de {maiorPeso:.1f}Kg.\n')