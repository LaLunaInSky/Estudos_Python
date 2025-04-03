from os import system

def obterFraseDigitadaPeloUsuário() -> str:
    frase_digitada: str = str(input("Escreva um frase: ")).strip()
    return frase_digitada.title()


def contarQuantidadeDeA(frase_digitada: str) -> int:
    quantidade_de_a: int = 0

    frase: str = frase_digitada.lower()

    for letra in frase:
        if (letra == 'a'):
            quantidade_de_a += 1

    return quantidade_de_a


def obterPrimeiraEÚltimaPosiçãoDoANaFrase(frase_digitada: str) -> list:
    frase: str = frase_digitada.lower()
    posições: list = []

    for x in range(len(frase)):
        if frase.find('a', x, len(frase)) != -1:
            posições.append(frase.find('a', x, len(frase)))

    if posições != []:
        return [posições[0], posições[-1]]
        
    else:
        posições.clear()
        return posições


def mostrarResultado(frase_digitada: str) -> None:
    posições_do_a: list = obterPrimeiraEÚltimaPosiçãoDoANaFrase(frase_digitada)

    print(f'''
    Analisando a frase {frase_digitada}...
A quantidade de letras \"A\" na frase é de {contarQuantidadeDeA(frase_digitada)}.''')

    if posições_do_a == []:
        print(f"A letra \"A\" não está em nenhuma posição.")
    else:
        print(f"A primeira ocorrência da letra \"A\" é na posição {posições_do_a[0] + 1}.\nA última ocorrência da letra \"A\" é na posição {posições_do_a[1] + 1}.\n")


def main() -> None:
    system("clear")

    frase_digitada_pelo_usuário: str = obterFraseDigitadaPeloUsuário()
    
    mostrarResultado(frase_digitada_pelo_usuário)


main()