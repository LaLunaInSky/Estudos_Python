#Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', 
#o programa se encerrará. OBS: use cores.

print(f'\n{'- Um programa de ajuda com informações dos módulos do Python -':^67}\n')

cores = (
    '\033[m',    #0 zerado
    '\033[41m',  #1 vermelho
    '\033[42m',  #2 verde
    '\033[43m',  #3 amarelo
    '\033[44m',  #4 azul
    '\033[45m',  #5 lilás
    '\033[46m',  #6 azul água
    '\033[47m',  #7 cinza
    '\033[7;40m' #8 branco
)

def ajuda(mensagem):
    título(f'Acessando o manual do comando \'{mensagem}\'', 3)
    print(cores[8], end='')
    help(mensagem)
    print(cores[0], end='')

def título(mensagem, cor=0):
    tamanho = len(mensagem) + 4
    print(cores[cor], end='')
    print(f'{'~' * tamanho}\n  {mensagem}\n{'~' * tamanho}', end='')
    print(cores[0])


while True:
    título('Sistema de Ajuda PyHelp', 5)
    resposta = input('Função ou Biblioteca> ').strip()

    if resposta == 'fim':
        print()
        break

    else:
       ajuda(resposta)
        