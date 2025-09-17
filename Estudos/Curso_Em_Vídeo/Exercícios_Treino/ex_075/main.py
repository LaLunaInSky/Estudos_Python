from os import system

def obterNúmeroInteiroDigitadoPeloUsuário(ordem_de_chamada_do_input: int = 1) -> int:
    número_inteiro_digitado_pelo_usuário: int = int(input(f"Digite o {ordem_de_chamada_do_input}º Número: "))

    return número_inteiro_digitado_pelo_usuário


def analisarQuantasVezesApareceuONúmeroNove(números_digitados: tuple) -> int:
    quantidade_de_vezes_que_o_número_nove_apareceu: int = 0

    for número in números_digitados:
        if número == 9:
            quantidade_de_vezes_que_o_número_nove_apareceu += 1

    return quantidade_de_vezes_que_o_número_nove_apareceu


def analisarQualFoiAPrimeiraPosiçãoQueONúmeroTrêsApareceu(números_digitados: tuple) -> str:
    contém_o_número_três: bool = False

    for número in números_digitados:
        if número == 3:
            contém_o_número_três = True
    
    if contém_o_número_três == False:
        return "não apareceu em nenhuma posição"
    else:
        return f"aparece pela primeira vez na posição {números_digitados.index(3) + 1}"


def analisarQuaisNúmeroSãoPares(números_digitados: tuple) -> list:
    números_pares_encontrados: list = []

    for número in números_digitados:
        if número % 2 == 0:
            números_pares_encontrados.append(número)

    return números_pares_encontrados


def mostrarInformaçõesSobreOsNúmerosDigitados(números_digitados: tuple) -> None:
    print(f"\nO número 9 apareceu {analisarQuantasVezesApareceuONúmeroNove(números_digitados)} vezes.")

    print(f"O número 3 {analisarQualFoiAPrimeiraPosiçãoQueONúmeroTrêsApareceu(números_digitados)}.")

    print(f"Os números pares digitados foram:", end="")

    números_pares_encontrados: list = analisarQuaisNúmeroSãoPares(números_digitados)

    if len(números_pares_encontrados) > 0:
        for número in números_pares_encontrados:
            print(f" {número}", end="")
    
    print(".\n")


def main() -> None:
    system("clear")

    quatro_números_digitados_pelo_usuário: tuple = (
        obterNúmeroInteiroDigitadoPeloUsuário(1),
        obterNúmeroInteiroDigitadoPeloUsuário(2),
        obterNúmeroInteiroDigitadoPeloUsuário(3),
        obterNúmeroInteiroDigitadoPeloUsuário(4)
    )

    mostrarInformaçõesSobreOsNúmerosDigitados(quatro_números_digitados_pelo_usuário)


main()