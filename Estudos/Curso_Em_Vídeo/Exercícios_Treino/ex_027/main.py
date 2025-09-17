from os import system

def obterNomeCompletoDoUsuário() -> str:
    nome_completo: str = str(input("Escreva o seu nome completo: ")).strip()
    return nome_completo.title()


def mostrarResultado(nome_completo: str) -> None:
    nome_separado: list = nome_completo.split(' ')
    
    print(f'''
Prazer em te conhecer {nome_completo}!
Seu primeiro nome é {nome_separado[0]},
e seu último nome é {nome_separado[-1]}.
''')


def main() -> None:
    system("clear")

    nome_completo_do_usuário = obterNomeCompletoDoUsuário()

    mostrarResultado(nome_completo_do_usuário)


main()