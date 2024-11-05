#Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em um lista, já na posição correta de inserção (sem usar o sort()). 
#No final, mostre a lista ordenada na tela.

print(f'\n{'- Me informe 5 números, e eu te devolvo eles na ordem -':^60}\n')

listaDeNúmerosOrdenados = []

for contagem in range(1, 6):
    while True:
        númeroDigitado = int(input(f'Qual o {contagem}º número? '))

        if númeroDigitado not in listaDeNúmerosOrdenados:
            break

        else:
            print('\033[31mNÚMERO JÁ ADICIONADO! Informe Outro...\033[m\n')

    if contagem == 1:
        listaDeNúmerosOrdenados.append(númeroDigitado)
        print('O número foi adicionado no final da lista...\n')
    
    else:
        if númeroDigitado < listaDeNúmerosOrdenados[0]:
            listaDeNúmerosOrdenados.insert(0, númeroDigitado)
            print('O número foi adiconado no começo da lista...\n')
        
        elif númeroDigitado > listaDeNúmerosOrdenados[-1]: 
            listaDeNúmerosOrdenados.append(númeroDigitado)
            print('O número foi adicionado no final da lista...\n')
        
        else:
            posiçãoAdicionar = contagem - len(listaDeNúmerosOrdenados)
            if númeroDigitado > listaDeNúmerosOrdenados[posiçãoAdicionar]:
                if númeroDigitado > listaDeNúmerosOrdenados[2]:
                    listaDeNúmerosOrdenados.insert(posiçãoAdicionar + 2, númeroDigitado)
                    print(f'O número foi adicionado na posição {posiçãoAdicionar + 2}...\n')
                else:
                    listaDeNúmerosOrdenados.insert(posiçãoAdicionar + 1, númeroDigitado)
                    print(f'O número foi adicionado na posição {posiçãoAdicionar + 1}...\n')
            else:
                listaDeNúmerosOrdenados.insert(posiçãoAdicionar, númeroDigitado)
                print(f'O número foi adicionado na posição {posiçãoAdicionar}...\n')
                
print(listaDeNúmerosOrdenados)