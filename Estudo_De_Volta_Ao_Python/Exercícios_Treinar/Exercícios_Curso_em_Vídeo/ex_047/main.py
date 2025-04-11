from os import system

def inicarContagemDeParesAtéCinquenta() -> None:
    for x in range(1, 51):
        if x % 2 == 0:
            if x == 50:
                print(f"{x}.\n")
            else:
                print(f"{x} -> ", end='')


def main() -> None:
    system("clear")

    inicarContagemDeParesAtéCinquenta()


main()