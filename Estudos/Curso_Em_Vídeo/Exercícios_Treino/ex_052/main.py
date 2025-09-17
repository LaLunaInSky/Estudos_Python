from os import system

def obterNúmeroPeloUsuário() -> int:
    número_digitado: int = int(input("Digite um número: "))
    return número_digitado


def mostrarResultado(número_digitado: int) -> None:
    print()
    
    vezes_divido: int = 0

    if número_digitado < 11:
        for x in range(1, 11):
            if número_digitado % x == 0:
                vezes_divido += 1

                print(f"[{x}]", end=' ')

            else:
                print(f"{x}", end=' ')
    else:
        for x in range(1, (número_digitado + 1)):
            if número_digitado % x == 0:
                vezes_divido += 1

                print(f"[{x}]", end=' ')

            else:
                print(f"{x}", end=' ')

    print(f"\n\nO número {número_digitado} foi divisivel {vezes_divido} vezes.")

    if vezes_divido == 2:
        if número_digitado % número_digitado == 0:
            if número_digitado % 1 == 0:
                print("É um número PRIMO!\n")
    else:
        print("NÃO é um número PRIMO!\n")


def main() -> None:
    system("clear")

    número_digitado_pelo_usuário: int = obterNúmeroPeloUsuário()

    mostrarResultado(número_digitado_pelo_usuário)


main()