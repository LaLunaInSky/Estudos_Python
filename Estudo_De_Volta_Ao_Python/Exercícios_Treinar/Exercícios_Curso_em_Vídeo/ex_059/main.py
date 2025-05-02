from os import system

def obterONúmeroInteiroDigitadoPeloUsuário(sequência_da_chamada_do_input: int = 1) -> int:
    número_inteiro_informado_pelo_usuário: int = int(input(f"Qual o {sequência_da_chamada_do_input}º Número Inteiro? "))
    
    return número_inteiro_informado_pelo_usuário


def obterOsDoisNúmerosInteirosDigitadoPeloUsuário() -> list:
    números_informado_pelo_usuário: list = [
        obterONúmeroInteiroDigitadoPeloUsuário(1),
        obterONúmeroInteiroDigitadoPeloUsuário(2)
    ]

    return números_informado_pelo_usuário


def somarNúmeros(x: int = 0, y: int = 1) -> str:
    return f"A Soma de {x} + {y} = {x + y} \n\n"


def multiplicarNúmeros(x: int = 1, y: int = 2) -> str:
    return f"A Multiplicação de {x} x {y} = {x * y} \n\n"


def informarONúmeroMaior(x: int = 1, y: int = 1) -> str:
    if x == y:
        return "Ambos são o mesmo número! \n\n"
    elif x > y:
        return f"O {x} é o número maior \n\n"
    else:
        return f"O {y} é o número maior \n\n"


def mostrarMenuComAsOpções(números_informados: list) -> None:
    resposta_da_escolha: str = ""
    
    while True:
        print(f'''{resposta_da_escolha}Com os números {números_informados[0]} e {números_informados[1]}, você gostaria de?    
        [ 1 ] Somar 
        [ 2 ] Multiplicar
        [ 3 ] Saber qual é o maior
        [ 4 ] Informar novos números
        [ 5 ] Fechar o programa''')

        opção_escolhida_pelo_usuário: int = int(input("Qual opção você escolhe? "))

        if opção_escolhida_pelo_usuário >= 1 and opção_escolhida_pelo_usuário <= 4:
            system("clear")

            if opção_escolhida_pelo_usuário == 1:
                resposta_da_escolha = somarNúmeros(números_informados[0], números_informados[1])
            
            elif opção_escolhida_pelo_usuário == 2:
                resposta_da_escolha = multiplicarNúmeros(números_informados[0], números_informados[1])

            elif opção_escolhida_pelo_usuário == 3:
                resposta_da_escolha = informarONúmeroMaior(números_informados[0], números_informados[1])

            else:
                números_informados = obterOsDoisNúmerosInteirosDigitadoPeloUsuário()
                resposta_da_escolha = ""

        elif opção_escolhida_pelo_usuário == 5:
            break
        else:
            system("clear")


def main() -> None:
    system("clear")

    números_informado_pelo_usuário: list = obterOsDoisNúmerosInteirosDigitadoPeloUsuário()

    mostrarMenuComAsOpções(números_informado_pelo_usuário)


main()