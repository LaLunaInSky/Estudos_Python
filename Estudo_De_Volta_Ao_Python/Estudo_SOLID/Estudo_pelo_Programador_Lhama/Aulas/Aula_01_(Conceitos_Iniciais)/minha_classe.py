from os import system

class MinhaClasse:
    #atributos
    def __init__(self, atributo_false_or_true: bool = False) -> None:
        self.atributo_um: str = "Meu atributo 1"
        self.atributo_dois: int = 123
        self.atributo_três: bool = atributo_false_or_true

        print("Objeto Construido com Sucesso!")


    #métodos
    def métodoUm(self) -> None:
        print("Minha ação 1!")

    
    def métodoDois(self) -> str:
        return "Minha ação 2!"


def main() -> None:
    system("clear")

    minha_classe_objeto: object = MinhaClasse(True)

    minha_classe_objeto.métodoUm()

    retorno_da_classe: str = minha_classe_objeto.métodoDois()

    print(retorno_da_classe)

    meus_atributos_da_classe: tuple = (
        minha_classe_objeto.atributo_um,
        minha_classe_objeto.atributo_dois,
        minha_classe_objeto.atributo_três
    )

    print(meus_atributos_da_classe)


main()