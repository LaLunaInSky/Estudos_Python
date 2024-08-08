#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre: 
#A)Quantos números foram digitados. B)A lista de valores, ordenada de forma decrescente. C)Se o valor 5 foi digitado ou não.

print(f'\n{'- Me informe quantos números quiser, e eu te devolvo algumas inforemações sobre os mesmos -':^96}\n')

listaDeNúmerosDigitados = []

while True:
    maisNúmero = 0
    
    while maisNúmero == len(listaDeNúmerosDigitados):
        númeroDigitado = int(input('Digite um número: '))

        if númeroDigitado not in listaDeNúmerosDigitados:
            listaDeNúmerosDigitados.append(númeroDigitado)
            print()
            break
        else:
            print('\033[31mNÚMERO JÁ ADICIONADO, tente outro!\033[m\n')

    perguntaSobreContinuar = input('Quer acrescentar mais um número(S/N)? ').strip().upper()

    if perguntaSobreContinuar in ('S', 'N'):
        if perguntaSobreContinuar == 'N':
            break
        else:
            maisNúmero += 1
    else:
        print('\033[31mAPENAS É ACEITO S (sim) OU N (não)!\033[m\n')

print(f'''
Foram digitados {len(listaDeNúmerosDigitados)} números.
Os números digitados em ordem decrescente: {sorted(listaDeNúmerosDigitados, reverse=True)}.''')

if listaDeNúmerosDigitados.count(5) != 0:
    print('O valor (5) foi digitado e está presente na lista.\n')
else:
    print('O valor (5) não foi digitado, portando não está presente na lista.\n')