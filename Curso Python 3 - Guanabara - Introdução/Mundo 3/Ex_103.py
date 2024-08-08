#Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. 
#O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

print(f'\n{'- Me informe o nome de um jogador e quantos gols ele fez, e eu te devolvo a ficha do mesmo -':^97}\n')

def ficha(nome, gols):
    if nome == '':
        nome = '<desconhecido>'

    if gols == '' or gols.isdecimal() == False:
        gols = '0'

    print(f'\nO jogador {nome} fez {gols} gols na partida.\n')


ficha(
    input(f'{'-'*40}\nQual o nome do jogador? ').capitalize(),
    input('Quantos gols fez? ')
)