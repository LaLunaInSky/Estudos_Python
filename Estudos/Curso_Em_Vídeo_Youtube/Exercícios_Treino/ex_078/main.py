from os import system

def obterONúmeroInteiroDigitadoPeloUsuário(ordem_da_sequência: int = 0) -> int:
    número_inteiro_digitado_pelo_usuário: int = int(input(f"Qual o número da posição {ordem_da_sequência}: "))

    return número_inteiro_digitado_pelo_usuário


def obterOsCincoNúmerosDigitadosPeloUsuário() -> list:
    números_digitados: list = []

    for contagem in range(0, 5):
        números_digitados.append(obterONúmeroInteiroDigitadoPeloUsuário(contagem))

    return números_digitados


def obterOMaiorEOMenorNúmeroDigitado(números_digitados: list) -> list:    
    o_número_maior_e_o_menor_da_sequência: list = []

    for posição, número in enumerate(números_digitados):
        if posição == 0:
            o_número_maior_e_o_menor_da_sequência.append(número)
            o_número_maior_e_o_menor_da_sequência.append(número)
        
        if o_número_maior_e_o_menor_da_sequência[0] < número:
            o_número_maior_e_o_menor_da_sequência[0] = número

        if o_número_maior_e_o_menor_da_sequência[1] > número:
            o_número_maior_e_o_menor_da_sequência[1] = número

    return o_número_maior_e_o_menor_da_sequência


def mostrarInformaçõesSobreOsNúmerosInformados(números_digitados: list) -> None:
    print(f"\nForam digitados os números: {números_digitados}")

    o_maior_e_o_menor_número_digitado: list = obterOMaiorEOMenorNúmeroDigitado(números_digitados)

    print(f"O maior número digitado foi o {o_maior_e_o_menor_número_digitado[0]} na posição {números_digitados.index(o_maior_e_o_menor_número_digitado[0]) + 1}.")
    print(f"O menor número digitado foi o {o_maior_e_o_menor_número_digitado[1]} na posição {números_digitados.index(o_maior_e_o_menor_número_digitado[1]) + 1}.\n")


def main() -> None:
    system("clear")

    números_digitados: list = obterOsCincoNúmerosDigitadosPeloUsuário()

    mostrarInformaçõesSobreOsNúmerosInformados(números_digitados)


main()