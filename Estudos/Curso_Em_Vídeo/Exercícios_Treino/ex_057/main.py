from os import system

def obterGêneroDoUsuário() -> str:
    while True:
        gênero: str = str(input("Qual o seu gênero [F/M]? ")).upper().strip()

        if gênero == "F" or gênero == "M":
            return gênero
        else:
            system("clear")

            print("Tente De novo.", end=" ")


def main() -> None:
    system("clear")

    gênero_do_usuário: str = obterGêneroDoUsuário()

    print("\nFIM!\n")


main()