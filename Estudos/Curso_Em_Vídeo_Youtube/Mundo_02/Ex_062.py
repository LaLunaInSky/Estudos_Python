#Melhore o Ex_061, perguntando para o usuário se ele quer mostrar mais algum termo. O programa encerra quando ele disser que quer mostrar 0 termos.

print(f'\n{'- Me informe o primeiro termo e a razão, e eu te devolvo a sua PA. Depois me informe quantos termos a mais você quer ver -':^127}\n')

primeiroTermoDaPA = int(input('Qaul o 1º Termo da PA? '))
razãoDaPA = int(input('Qual a Razão da PA? '))
próximoTermoDaPA = primeiroTermoDaPA
contador = 1
quantosTermosAMais = 10
totalDeTermosMostrados = quantosTermosAMais

print()

while quantosTermosAMais != 0:
    if contador == quantosTermosAMais:
        print(f'{próximoTermoDaPA}\n')
    else:
        print(f'{próximoTermoDaPA} -> ', end='')
    próximoTermoDaPA += razãoDaPA

    if contador != quantosTermosAMais:
        contador += 1
    else:
        quantosTermosAMais = int(input('Quantos termos você quer ver a mais? '))
        totalDeTermosMostrados += quantosTermosAMais
        contador = 1

print(f'\nForam mostrados {totalDeTermosMostrados} termos da PA acima.\n')