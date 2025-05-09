from os import system

class Pessoa:
    def __init__(self, informe_a_altura_desta_pessoa: float, informe_o_cpf_desta_pessoa: str) -> None:
        self.__altura_da_pessoa: float = informe_a_altura_desta_pessoa
        self.__cpf_da_pessoa: str = informe_o_cpf_desta_pessoa

    
    def apresentarAPessoa(self) -> None:
        print(f"Olá! Minha Altura é de {self.__altura_da_pessoa:.2f}m,")

        self.__apresentarDocumentoDaPessoa()


    def __apresentarDocumentoDaPessoa(self) -> None:
        print(f"e o meu documento é o cpf {self.__cpf_da_pessoa}.")


    def getNumberOfCPF(self) -> str:
        return self.__cpf_da_pessoa


def main() -> None:
    system("clear")

    pessoa_um: object = Pessoa(1.75, "000.000.000-00")

    pessoa_um.apresentarAPessoa()

    #quando o atributo é privado, ele é inateralvel por atribuição de variável
    pessoa_um.__altura_da_pessoa = 1.5
    pessoa_um.__cpf_da_pessoa = "500"

    print()

    print(pessoa_um.__altura_da_pessoa, pessoa_um.__cpf_da_pessoa)

    print()

    print(pessoa_um.__altura_da_pessoa, pessoa_um.__cpf_da_pessoa)

    print()

    pessoa_um.apresentarAPessoa()

    print()

    print(pessoa_um.__altura_da_pessoa, pessoa_um.__cpf_da_pessoa)
    print(pessoa_um.getNumberOfCPF())


main()