from os import system
from time import sleep

def iniciarContagemRegressiva() -> None:
    for x in range(0, 11):
        print(10 - x)
        sleep(1)


def main() -> None:
    system("clear")

    iniciarContagemRegressiva()

    print("BOOOOOM!")


main()