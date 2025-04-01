from os import system

def add2(x: int) -> int:
    return x + 2


def main() -> None:
    system("clear")

    número_x: int = 3
    soma_1: int = add2(número_x)

    print(f"{número_x} + 2 = {soma_1}")


main()