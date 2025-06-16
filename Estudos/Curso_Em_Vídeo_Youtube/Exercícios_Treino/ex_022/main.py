from os import system
from time import sleep

def obterNomeCompletoDoUsuário() -> str:
    nome_completo_usuário: str = str(input("Escreva o seu nome completo: "))
    return nome_completo_usuário


def separaNome(nome_completo:str) -> list:
    nome_separado: list = nome_completo.split(' ')
    return nome_separado


def mostrarResultado(nome_completo) -> None:
    nome_separado: list = separaNome(nome_completo)

    total_de_letras: int = 0

    for nome in nome_separado:
        total_de_letras += len(nome)

    
    print(f'''
Seu nome todo em maiúscula é {nome_completo.upper()}.
Seu nome todo em minúscula é {nome_completo.lower()}.
Seu nome possui ao todo {total_de_letras} letras.
Seu primeiro nome {nome_separado[0].title()} possui {len(nome_separado[0])} letras.
''')


def main() -> None:
    system("clear")

    nome_completo = obterNomeCompletoDoUsuário()
    
    print("\nAnalisando o seu nome...")
    
    sleep(2)

    mostrarResultado(nome_completo)


main()