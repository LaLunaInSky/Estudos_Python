#Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens 
#através da função criada: A)De 1 até 10, de 1 em 1; B)De 10 até 0, de 2 em 2; C)Uma contagem personalizada.

from time import sleep

print(f'\n{'- Me informe quais números você quer que eu conte, e de quanto em quanto preciso pular -':^93}')

def contador(início, final, pulo):
    if pulo == 0:
        pulo = 1
    
    elif pulo < 0:
        pulo = -(pulo)
        
    print()

    sleep(0.5)
    print(f'Contando de {início} à {final}, pulando de {pulo} em {pulo}:')
    sleep(1)


    if final > início:
        final += 1

    elif final < início:
        pulo = -(pulo)
        final -= 1

    for contagem in range(início, final, pulo):
        sleep(0.5)
        print(contagem, end=' ')
    
    sleep(0.2)
    print()

contador(1, 10, 1)
contador(10, 0, 2)

sleep(0.5)

print('\nAgora é sua vez, escolha os números para eu contar!')

sleep(2)

contador(
    int(input('Qual o número inicial da contagem? ')),
    int(input('Qaul o número final da contagem? ')),
    int(input('De quanto em quanto irei contar? '))
)

print()