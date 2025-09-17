from os import system
from random import shuffle

def obterNomeDoAluno(número_chamada: int) -> str:
    nome_aluno = str(input(f"Escreva o nome do {número_chamada}º Aluno: "))
    return nome_aluno.title()


def mostrarResultado(lista_alunos: list) -> None:
    print("\nOrdem de Apresentação:")
    for index, aluno in enumerate(lista_alunos):
        print(f"{index + 1}º - {aluno}")
        

def main() -> None:
    system("clear")

    lista_nome_de_alunos: list = []

    for x in range(4):
        lista_nome_de_alunos.append(obterNomeDoAluno(x + 1))

    shuffle(lista_nome_de_alunos)
    
    mostrarResultado(lista_nome_de_alunos)


main()