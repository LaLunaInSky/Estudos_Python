#Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seus programa tem analisar todos os valores 
#e dizer qual deles é o maior.

from time import sleep

print(f'\n{'- Me informe quantos números quiser, e eu te direi qual é o maior entre eles -':^83}\n')

def maior(*números):
    sleep(1)
    print('Analisando os números informados: ')
    sleep(0.5)

    if len(números) != 0:

        for contagem in range(0, len(números)):
            print(f'{números[contagem]}', end=' ')
            sleep(0.5)
    
    else:
        sleep(0.5)
        print('Nada informado!', end=' ')

    print('→', end=' ')


    if len(números) == 1 or len(números) == 0:
        print(f'Foi informado {len(números)}', end=' ')
        if len(números) == 1:
            print('número.')
        else:
            print('números.')
    
    else:
        print(f'Foram informados {len(números)} números.')

    sleep(0.5)
    print('O maior número informado é', end=' ')

    if len(números) == 0:
        print('nenhum.')
    else:
        print(f'o {max(números)}.')

    print()

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()