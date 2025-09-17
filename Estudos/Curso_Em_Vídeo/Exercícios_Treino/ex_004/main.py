from os import system

def getUserInput():
    input_user = input("Digite algo: ")
    return input_user


def obterClasse(algo_digitado):
    return type(algo_digitado)


def traduzirBool(boolean):
    if (boolean):
        return "Verdade"
    else:
        return "Falso"


def verificarSeÉApenasEspaços(algo_digitado):
    return traduzirBool(algo_digitado.isspace())


def verificarSeÉApenasNúmeros(algo_digitado):
    return traduzirBool(algo_digitado.isnumeric())


def verificarSeÉApenasLetras(algo_digitado):
    return traduzirBool(algo_digitado.isalpha())


def verificarSePossuiLetrasENúmeros(algo_digitado):
    return traduzirBool(algo_digitado.isalnum())


def verificarSeEstáMaiúscula(algo_digitado):
    return traduzirBool(algo_digitado.isupper())


def verificarSeEstáMinúscula(algo_digitado):
    return traduzirBool(algo_digitado.islower())


def verificarSeEstáCapitalizada(algo_digitado):
    return traduzirBool(algo_digitado.istitle())


def mostrarCaracterísticas(algo_digitado):
    print(f'''
    As Características de \'{algo_digitado}\'

O tipo primitivo é {obterClasse(algo_digitado)}
É apenas espaço? {verificarSeÉApenasEspaços(algo_digitado)}
É apenas números? {verificarSeÉApenasNúmeros(algo_digitado)}
É apenas letras? {verificarSeÉApenasLetras(algo_digitado)}
Possui letras e números? {verificarSePossuiLetrasENúmeros(algo_digitado)}
Está em maiúscula? {verificarSeEstáMaiúscula(algo_digitado)}
Está em minúscula? {verificarSeEstáMinúscula(algo_digitado)}
Está capitalizada? {verificarSeEstáCapitalizada(algo_digitado)}
''')


def main():
    system("clear")

    algo_digitado = getUserInput()

    mostrarCaracterísticas(algo_digitado)


main()