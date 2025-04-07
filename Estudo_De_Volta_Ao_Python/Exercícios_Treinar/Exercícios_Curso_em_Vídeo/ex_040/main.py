from os import system

def obterNotaDoAluno(sequência: int = 1) -> float:
    while True:
        nota_aluno: float = float(input(f"Qual a {sequência}ª Nota? "))

        if nota_aluno >= 0 and nota_aluno <= 10:
            return round(nota_aluno, 1)
        else:
            system("clear")


def calcularAMédiaDoAluno(nota_1: float = 0, nota_2: float = 0) -> float:
    return round(((nota_1 + nota_2) / 2), 1)


def analisarEstadoDeAprovaçãoDoAluno(média: float = 0) -> str:
    if média < 5:
        return "REPROVADO"
    elif média >= 7:
        return "APROVADO"
    else:
        return "de RECUPERAÇÃO"


def mostrarResultado(notas_do_aluno: dict) -> None:
    print(f'''
O aluno com as notas {notas_do_aluno["nota_1"]} e {notas_do_aluno["nota_2"]} ficou com a média de {notas_do_aluno["média"]},
o aluno então está {notas_do_aluno["estado_de_aprovação"]}.
''')


def main() -> None:
    system("clear")

    notas_do_aluno: dict = {
        "nota_1": 0, 
        "nota_2": 0, 
        "média": 0, 
        "estado_de_aprovação": ''
    }

    for x in range(1, 3):
        notas_do_aluno[f"nota_{x}"] = obterNotaDoAluno(x)

    notas_do_aluno["média"] = calcularAMédiaDoAluno(notas_do_aluno["nota_1"], notas_do_aluno["nota_2"])

    notas_do_aluno["estado_de_aprovação"] = analisarEstadoDeAprovaçãoDoAluno(notas_do_aluno["média"])

    mostrarResultado(notas_do_aluno)


main()