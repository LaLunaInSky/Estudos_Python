from os import system
from random import randint

def obterONúmeroInteiroEntreUmADezDigitadoPeloUsuário() -> int:
    while True:
        número_inteiro_entre_um_a_dez: int = int(input("Qual número você escolhe [Só vale entre 1 a 10]? "))

        if número_inteiro_entre_um_a_dez <= 10 and número_inteiro_entre_um_a_dez >= 1:
            return número_inteiro_entre_um_a_dez
        else:
            system("clear")


def obterSeOUsuárioQuerParOuÍmpar() -> str:
    while True:
        escolha_par_ou_ímpar_do_usuário: str = str(input("Você escolhe Par ou Ímpar [P/I]? ")).lower()

        if escolha_par_ou_ímpar_do_usuário == 'p' or escolha_par_ou_ímpar_do_usuário == 'i':
            return escolha_par_ou_ímpar_do_usuário


def obterONúmeroInteiroEntreUmADezDoComputador() -> int:
    número_entre_um_e_dez_do_computador: int = randint(1, 10)
    
    return número_entre_um_e_dez_do_computador


def definirParOuÍmparDoComputador(par_ou_ímpar_do_usuário: str) -> str:
    if par_ou_ímpar_do_usuário == 'p':
        return 'i'
    elif par_ou_ímpar_do_usuário == 'i':
        return 'p'


def somarOsDoisNúmerosInteiros(número_do_usuário: int, número_do_computador: int) -> int:
    soma_dos_números: int = número_do_usuário + número_do_computador

    return soma_dos_números


def analisarSeONúmeroSomadoÉParOuÍmpar(soma_dos_números: int) -> str:
    if soma_dos_números % 2 == 0:
        return 'p'
    else:
        return 'i'
    

def analisarQuemGanhouAPartida(par_ou_ímpar_do_usuário: str, par_ou_ímpar_do_computador: str, par_ou_ímpar_da_soma_dos_números: str) -> str:
    if par_ou_ímpar_do_usuário == par_ou_ímpar_da_soma_dos_números:
        return "Jogador"
    elif par_ou_ímpar_do_computador == par_ou_ímpar_da_soma_dos_números:
        return "Computador"
    

def transformarPOuIEmParOuÍmpar(vogal_única: str) -> str:
    if vogal_única == 'p':
        return "PAR"
    elif vogal_única == 'i':
        return "ÍMPAR"


def analisarSeOJogoContinuará() -> None:
    partidas_ganha_pelo_usuário: int = 0

    while True:
        número_digitado_pelo_usuário: int = obterONúmeroInteiroEntreUmADezDigitadoPeloUsuário()
        escolha_par_ou_ímpar_do_usuário: str = obterSeOUsuárioQuerParOuÍmpar()

        número_sorteado_do_computador: int = obterONúmeroInteiroEntreUmADezDoComputador()
        par_ou_ímpar_do_computador: str = definirParOuÍmparDoComputador(escolha_par_ou_ímpar_do_usuário)

        soma_dos_números_jogados: int = somarOsDoisNúmerosInteiros(número_digitado_pelo_usuário, número_sorteado_do_computador)
        par_ou_ímpar_da_soma_dos_números_jogados: str = analisarSeONúmeroSomadoÉParOuÍmpar(soma_dos_números_jogados)

        ganhador_da_partida: str = analisarQuemGanhouAPartida(escolha_par_ou_ímpar_do_usuário, par_ou_ímpar_do_computador, par_ou_ímpar_da_soma_dos_números_jogados)

        print(f'''
Você jogou {número_digitado_pelo_usuário} e escolheu {transformarPOuIEmParOuÍmpar(escolha_par_ou_ímpar_do_usuário)}!
O Computador jogou {número_sorteado_do_computador} e escolheu {transformarPOuIEmParOuÍmpar(par_ou_ímpar_do_computador)}!

O total deu {soma_dos_números_jogados} logo é {transformarPOuIEmParOuÍmpar(par_ou_ímpar_da_soma_dos_números_jogados)}...
''')

        if ganhador_da_partida == "Jogador":
            partidas_ganha_pelo_usuário += 1
            
            print("Você GANHOU! \n\nVamos Jogar mais uma vez.")

        else:
            print(f"Você PERDEU! Você ganhou {partidas_ganha_pelo_usuário} vezes.\n")
            break


def main() -> None:
    system("clear")

    analisarSeOJogoContinuará()


main()