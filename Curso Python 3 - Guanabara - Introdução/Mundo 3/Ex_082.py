#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores 
#ímpares dgitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

print(f'\n{'- Me informe quantos números quiser, e eu te devolvo os pares e os ímpares entre eles -':^92}\n')

listaDeNúmerosDigitados = []
listaDeNúmerosPares = []
listaDeNúmerosÍmpares = []
acrescentarMaisUmNúmero = 0

while True:
    while acrescentarMaisUmNúmero == len(listaDeNúmerosDigitados):
        númeroDigitado = int(input('Me informe um número: '))

        if númeroDigitado not in listaDeNúmerosDigitados:    
            listaDeNúmerosDigitados.append(númeroDigitado)
            break
        else:
            print('\033[31mNÚMERO JÁ DIGITADO! Me informe outro.\033[m\n')

    perguntaSobreContinuar = input('Quer acrescentar mais um número(S/N)? ').strip().lower()

    if perguntaSobreContinuar in ('s', 'n'):
        if perguntaSobreContinuar == 'n':
            break
        else:
            acrescentarMaisUmNúmero += 1

    else:
        print('\033[31mAPENAS É ACEITO S (sim) OU N (não)!\033[m\n')

for item in listaDeNúmerosDigitados:
    if item % 2 == 0:
        listaDeNúmerosPares.append(item)
    else:
        listaDeNúmerosÍmpares.append(item)

print(f'''
Os números digitados foram os: {sorted(listaDeNúmerosDigitados)}.
Os números Pares foram os: {sorted(listaDeNúmerosPares)}.
Os números Ímpares foram os: {sorted(listaDeNúmerosÍmpares)}.
''')