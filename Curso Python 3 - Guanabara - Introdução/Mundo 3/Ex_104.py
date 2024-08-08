#Crie um programa que tenha a função leiaInteiro(), que vai funcionar de forma semelhante à função input() do Python, só que fazendo a validação para aceitar 
#apenas um valor numérico.

print(f'\n{'- Me informe um número, e eu te devolvo o resultado caso ele seja mesmo um número inteiro -':^96}\n')

def leiaInteiro(texto):
    while True:
        númeroDigitado = input(f'{texto}').strip()

        if númeroDigitado.isdecimal():
            break
        
        else:
            print('\033[31mAPENAS É ACEITO NÚMERO INTEIRO!\033[m\n')
            
    return númeroDigitado


númeroDigitado = leiaInteiro('Digite um número: ')

print(f'\nVocê digitou o número {númeroDigitado}.\n')