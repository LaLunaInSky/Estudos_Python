# 87-1.97-22.4 Normal, 120-1.75-39.2 Obesidade, 150-1.60-58.6 Obesidade mórbida, 45-1.80-13.9 Abaixo

from os import system

def obterPesoDoUsuário() -> float:
    peso: float = float(input("Qual o seu peso (Kg)? "))
    return peso


def obterAlturaDoUsuário() -> float:
    altura: float = float(input("Qual a sua altura (m)? "))
    return altura


def calcularIMCDoUsuário(peso: float, altura: float) -> float:
    return round((peso / (altura ** 2)), 2)


def definirStatusCorporalDoUsuário(IMC: float) -> str:
    if IMC < 18.5:
        return "Abaixo do Peso"
    elif IMC < 25:
        return "Peso Ideal"
    elif IMC < 30:
        return "Sobrepeso"
    elif IMC < 40:
        return "Obesidade"
    else:
        return "Obesidade Mórbida"


def mostrarResultado(dados_do_usuário: dict) -> None:
    print(f'''
A pessoa com {dados_do_usuário["peso"]:.2f}Kg e {dados_do_usuário["altura"]:.2f}m,
tem o IMC de {dados_do_usuário["IMC"]:.2f}, logo {dados_do_usuário["status_corporal"]}.
''')


def main() -> None:
    system("clear")

    dados_do_usuário: dict = {
        "peso": 0,
        "altura": 0,
        "IMC": 0,
        "status_corporal": ''
    }

    dados_do_usuário["peso"] = obterPesoDoUsuário()
    
    dados_do_usuário["altura"] = obterAlturaDoUsuário()

    dados_do_usuário["IMC"] = calcularIMCDoUsuário(
        dados_do_usuário["peso"],
        dados_do_usuário["altura"]
    )

    dados_do_usuário["status_corporal"] = definirStatusCorporalDoUsuário(
        dados_do_usuário["IMC"]
    )

    mostrarResultado(dados_do_usuário)


main()