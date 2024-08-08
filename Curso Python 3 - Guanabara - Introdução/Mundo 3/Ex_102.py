#Crie um programa que tenho uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e o outro chamado mostrar, 
#que será um valor lógico(opcional) indidando se será mostrado ou não na tela o processo de cálculo do fatorial.

print(f'\n{'- Me informe um número qeu você queira saber o fatorial, e me informe também se quer ver a conta -':^103}\n')

def fatorial(número, mostrar=False):
    print(f'{número}! =', end=' ')

    for contagem in range(número, 0, -1):
        if mostrar == True:
            if contagem != 1:
                print(f'{contagem} x', end=' ')
            else:
                print(f'{contagem} =', end=' ')

        if contagem < número:
            número *= contagem

    return print(número, '\n')

fatorial(
    int(input('Qual o número? ')),
    mostrar=bool(input('Quer mostar a expressão inteira (x = Sim, nada = Não)? '))
)