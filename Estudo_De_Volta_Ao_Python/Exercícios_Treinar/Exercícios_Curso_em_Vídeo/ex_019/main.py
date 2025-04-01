from os import system
from random import choice

def obterNomeDoAluno(número_contagem: int) -> str:
    input_nome_aluno = str(input(f"Nome do {número_contagem}º Aluno: "))
    return input_nome_aluno.title()


def sortearNome(lista_nomes: list) -> str:
    nome_sorteado = choice(lista_nomes)
    return nome_sorteado


def mostrarResultados(nome_sorteado: str) -> None:
    print(f'''
O aluno sorteado é {nome_sorteado}.
''')


def main() -> None:
    system("clear")

    lista_de_alunos: list = []

    for x in range(4):
        lista_de_alunos.append(obterNomeDoAluno(x + 1))

    nome_sorteado = sortearNome(lista_de_alunos)

    mostrarResultados(nome_sorteado)


main()