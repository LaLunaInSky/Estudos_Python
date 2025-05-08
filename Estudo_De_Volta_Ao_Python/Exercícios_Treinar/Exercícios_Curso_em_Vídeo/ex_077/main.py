from os import system

def obterPalavrasDaTupla() -> tuple:
    palavras: tuple = (
        "aprender", "programar", "linguagem", "python", "curso", "gratis", "estudar", "praticar", "trabalhar", "mercado", "programador", "futuro"
    )

    return palavras


def analisarAsVogaisDaPalavra(palavra: str) -> list:
    vogais_da_palavra: list = []
    
    for letra in palavra:
        if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
            vogais_da_palavra.append(letra)

    return vogais_da_palavra


def mostrarInformaçõesDaPalavras(palavras_selecionadas: tuple) -> None:
    for palavra in palavras_selecionadas:
        print(f"A palavra {palavra.upper()} tem as vogais:", end="")

        vogais_da_palavra: list = analisarAsVogaisDaPalavra(palavra)

        for vogal in vogais_da_palavra:
            print(f" {vogal}", end='')

        print()


def main() -> None:
    system("clear")

    palavras_selecionadas: tuple = obterPalavrasDaTupla()

    mostrarInformaçõesDaPalavras(palavras_selecionadas)


main()