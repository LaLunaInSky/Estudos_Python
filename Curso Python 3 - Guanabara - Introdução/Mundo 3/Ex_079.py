#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. 
#No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

print(f'\n{'- Me informe quantos números quiser, e eu te devolvo eles em ordem -':^73}\n')

listaDeNúmerosDigitados = []

while True:
    while True:
        númeroDigitado = int(input('Digite um número: '))

        if listaDeNúmerosDigitados.count(númeroDigitado) == 0:
            listaDeNúmerosDigitados.append(númeroDigitado)
            break
        else:
            print('\033[31mNÚMERO JÁ ADICIONADO, valor será descartado!\033[m\n')

    pergutaSobreContinuar = input('Quer acrescentar mais um número(S/N)? ').strip().upper()

    if pergutaSobreContinuar in ('S', 'N'):
        if pergutaSobreContinuar == 'N':
            break
    else:
        print('\033[31mAPENAS S (sim) OU N (não)!\033[m\n')

print(f'\nOs números digitados foram os {sorted(listaDeNúmerosDigitados)}.\n')