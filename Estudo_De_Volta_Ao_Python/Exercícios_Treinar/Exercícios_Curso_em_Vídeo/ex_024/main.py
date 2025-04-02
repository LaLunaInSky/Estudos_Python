from os import system
from time import sleep

def obterNomeDaCidadeQueOUsuárioNasceu() -> str:
    nome_cidade_usuário = str(input("Em que cidade você nasceu? "))
    return nome_cidade_usuário.title()


def analisarFraseProcurandoSantoNoPrimeiroNome(nome_cidade: str) -> str:
    nome_cidade_separado = nome_cidade.lower().split(' ')
    
    if nome_cidade_separado[0].find("santo") == 0:
        return ''
    
    elif nome_cidade_separado[0].find("santo") == -1:
        return "não "
        

def mostrarResultado(nome_cidade: str) -> None:
    resposta: str = analisarFraseProcurandoSantoNoPrimeiroNome(nome_cidade)

    sleep(1)

    print(f'''
A cidade {resposta}começa com o nome "SANTO".
''')


def main() -> None:
    system("clear")

    nome_da_cidade: str = obterNomeDaCidadeQueOUsuárioNasceu()

    print(f"Analisando a sua cidade {nome_da_cidade}...")

    mostrarResultado(nome_da_cidade)


main()