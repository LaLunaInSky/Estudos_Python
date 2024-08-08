#Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
#Ex: escreva('Olá, Mundo!)
#~~~~~~~~~~~~~~~
#  Olá, Mundo!
#~~~~~~~~~~~~~~~

print(f'\n{'- Me informe uma frase, e eu irei formatar ela -':^52}\n')

def escreva(texto):
    tamanho = len(texto) + 4
    print(f'\n{'~'*tamanho}\n{'  ' + texto.title()}\n{'~'*tamanho}\n')


escreva(input('Escreva uma frase: '))