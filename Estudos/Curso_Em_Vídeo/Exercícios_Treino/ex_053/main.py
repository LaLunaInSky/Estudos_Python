from os import system

def obterFraseDigitadoPeloUsuário() -> str:
    frase_digitada: str = str(input("Digite um frase: "))
    return frase_digitada.replace(' ', '').strip().upper()


def mostrarResultado(frase_digitada: str) -> None:
    repsosta: str = ''
    
    if frase_digitada != frase_digitada[::-1]:
        repsosta: str = "NÃO "
    
    print(f'''
A frase {frase_digitada} de trás para frente fica {frase_digitada[::-1]},
logo essa frase {repsosta}é PALÍNDROMA!
''')


def main() -> None:
    system("clear")

    frase_digitada_pelo_usuário: str = obterFraseDigitadoPeloUsuário()

    mostrarResultado(frase_digitada_pelo_usuário)


main()