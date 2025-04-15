from os import system

def obterNomeIdadeEPesoPeloUsuário(sequência: int = 0) -> dict:
    dados_da_pessoa: dict = {}
    
    print(f"{"=" * 5}{f" {sequência}ª Pessoa "}{"=" * 5}")

    dados_da_pessoa["nome"] = str(input("Nome: "))
    dados_da_pessoa["idade"] = int(input("Idade: "))

    while True:
        dados_da_pessoa["gênero"] = str(input("Gênero [F/M]: ")).upper().strip()
        print(dados_da_pessoa["gênero"])

        if dados_da_pessoa["gênero"] == "M" or dados_da_pessoa["gênero"] == "F":
            return dados_da_pessoa
        else:
            #system("clear")

            print(f"{"=" * 5}{f" {sequência}ª Pessoa "}{"=" * 5}\nNome: {dados_da_pessoa["nome"]}\nIdade: {dados_da_pessoa["idade"]}")


def calcularMédiaDeIdadeDoGrupoDePessoas(lista_de_dados_de_pessoas: list) -> float:
    soma_das_idades: float = 0
    
    for pessoa in lista_de_dados_de_pessoas:
        soma_das_idades += pessoa["idade"]

    média_das_idades: float = soma_das_idades / len(lista_de_dados_de_pessoas)
    return média_das_idades


def analisarQuemÉOHomemMaisVelho(lista_de_dados_de_pessoas: list) -> dict:
    homens_do_grupo: list = []
    idades: list = []
    
    for pessoa in lista_de_dados_de_pessoas:
        if pessoa["gênero"] == "M":
            homens_do_grupo.append({"nome":pessoa["nome"], "idade": pessoa["idade"]})

    for homem in homens_do_grupo:
        idades.append(homem["idade"])

    idades.sort()

    for homem in homens_do_grupo:
        if homem["idade"] == idades[-1]:
            return homem
        

def analisarAsMulheresDoGrupoComMenosDeVinte(lista_de_dados_de_pessoas: list) -> list:
    quantidade_de_mulheres_com_menos_de_vinte: int = 0

    for pessoa in lista_de_dados_de_pessoas:
        if pessoa["gênero"] == "F" and pessoa["idade"] < 20:
            quantidade_de_mulheres_com_menos_de_vinte += 1

    if quantidade_de_mulheres_com_menos_de_vinte > 0:
        return ["", f"{quantidade_de_mulheres_com_menos_de_vinte} "]
    else:
        return ["não ", ""]


def mostrarResultado(lista_de_dados_de_pessoas: list) -> None:
    homem_mais_velho_do_grupo: dict = analisarQuemÉOHomemMaisVelho(lista_de_dados_de_pessoas)

    lista_de_mulheres_abaixo_de_vinte: list = analisarAsMulheresDoGrupoComMenosDeVinte(lista_de_dados_de_pessoas)

    print(f'''A média de idade do grupo é de {calcularMédiaDeIdadeDoGrupoDePessoas(lista_de_dados_de_pessoas)} anos.
O homem mais velho do grupo é o {homem_mais_velho_do_grupo["nome"]} que tem {homem_mais_velho_do_grupo["idade"]} anos.
No grupo {lista_de_mulheres_abaixo_de_vinte[0]}possui {lista_de_mulheres_abaixo_de_vinte[1]}mulheres com menos de 20 anos.
''')


def main() -> None:
    system("clear")

    dados_das_pessoas: list = []

    for count in range(1, 5):
        dados_das_pessoas.append(obterNomeIdadeEPesoPeloUsuário(count))
        
        system("clear")

    mostrarResultado(dados_das_pessoas)


main()