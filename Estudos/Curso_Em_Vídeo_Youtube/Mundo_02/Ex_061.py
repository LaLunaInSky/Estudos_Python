#Refaça o Ex_051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

print(f'\n{'- Me informe o primeiro termo e a razão, e eu te devolvo a sua PA -':^72}\n')

primeiroTermoDaPA = int(input('Qual o 1º Termo da PA? '))
razãoDaPA = int(input('Qaul a razão da PA? '))
próximoTermoDaPA = primeiroTermoDaPA
contador = 1

print()

while contador != 11:
    
    if contador == 10:
        print(f'{próximoTermoDaPA}\n')
    else:
        print(f'{próximoTermoDaPA} -> ', end='')
    
    contador += 1

    próximoTermoDaPA += razãoDaPA
