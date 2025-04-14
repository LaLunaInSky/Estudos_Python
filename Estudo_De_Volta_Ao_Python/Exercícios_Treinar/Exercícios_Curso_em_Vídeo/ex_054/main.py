from os import system
from datetime import datetime

ano_atual: int = datetime.now().year
ano_maioridade: int = ano_atual - 18

def obterAnoDeNascimento(sequência: int = 0) -> int:
    ano_de_nascimento: int  = int(input(f"Qual o ano de nascimento da {sequência}ª Pessoa? "))
    return ano_de_nascimento


def mostrarResultado(menores: list, maiores: list) -> None:
    print(f'''
Foram digitados {len(menores)} menores que a maioridade,
e foram digitados {len(maiores)} maiores que a maioridade.
''')


def main() -> None:
    system("clear")

    menores_de_maioridade: list = []
    maiores_de_maioridade: list = []

    for count in range(1, 8):
        ano_digitado: int = obterAnoDeNascimento(count)
        
        if ano_digitado <= ano_maioridade:
            maiores_de_maioridade.append(ano_digitado)
        else: 
            menores_de_maioridade.append(ano_digitado)

    mostrarResultado(menores_de_maioridade, maiores_de_maioridade)
    

main()