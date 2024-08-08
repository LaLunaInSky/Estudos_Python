#Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. 
#No final, mostre os valores pares e ímpares em ordem crescente.

print(f'\n{'- Me informe 7 números, e eu te digo quais são pares e ímpares -':^69}\n')

listaDeNúmeros = [[], []]

for contagem in range(1, 8):
    while True:
        número = int(input(f'Qual o {contagem}º número? '))

        if número not in listaDeNúmeros[0] and número not in listaDeNúmeros[1]:
            break
        else:
            print(f'\033[31mO NÚMERO ({número}) JÁ FOI DIGITADO! Tente outro...\033[m\n')
    
    if número % 2 == 0:
        listaDeNúmeros[0].append(número)
    else:
        listaDeNúmeros[1].append(número)

print(f'''
Os números pares digitados foram: {sorted(listaDeNúmeros[0])}.
Os números ímpares digitados foram: {sorted(listaDeNúmeros[1])}.
''')