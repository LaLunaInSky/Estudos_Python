from os import system

def obterQuantidadeDeNotas():
    input_quantidade = int(input("Quantas notas você irá adicionar? "))
    return input_quantidade


def obterEntradaIntDoUsuário(nota=0):
    input_user = float(input(f"Digite a {nota}ª Nota: "))
    return input_user


def obterNotas(quantidade_de_notas):
    notas = []

    for x in range(quantidade_de_notas):
        notas.append(obterEntradaIntDoUsuário(x + 1))

    return notas


def obterMédiaDasNotas(notas):
    soma = 0

    for nota in notas:
        soma += nota

    return round((soma / len(notas)), 1)


def mostrarResultado(notas, média_notas):
    print(f"\nO aluno com as notas", end=" ")

    for nota in notas:
        print(f"{nota},", end=" ")

    print(f"a sua média é {média_notas}.\n")


def main():
    system("clear")

    quantidade_de_notas = obterQuantidadeDeNotas()
    notas = obterNotas(quantidade_de_notas)
    média_notas = obterMédiaDasNotas(notas)

    mostrarResultado(notas, média_notas)

main()