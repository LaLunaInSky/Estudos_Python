# 3-4-5 Escaleno, 4-3-4 Isósceles, 7-7-7 Equilátero, 1-9-8 não forma

from os import system

def obterSegmento(sequência: int = 1) -> float:
    segmento: float = float(input(f"{sequência}º Segmento: "))
    return round(segmento, 1)


def analisarSeFormaUmTriângulo(a: int = 0, b: int = 0, c: int = 0) -> bool:
    if (a < (b + c)) and (b < (a + c)) and (c < (a + b)):
        return True
    else:
        return False
    

def definirQualTipoDeTriânguloÉ(a: int = 0, b: int = 0, c: int = 0) -> str:
    if a == b and b == c:
        return "Equilátero"
    elif (a == b) or (a == c) or (b == c):
        return "Isósceles"
    else:
        return "Escaleno"


def mostrarResultado(dados_dos_segmentos: dict) -> None:
    mensagem_de_retorno: str = ''
    
    if dados_dos_segmentos["é_um_triângulo"]:
        mensagem_de_retorno = f"FORMAM um Triângulo {dados_dos_segmentos["tipo_do_triângulo"]}"
    else:
        mensagem_de_retorno = "NÃO FORMAM um Triângulo"

    
    print(f'''
Os segmentos {dados_dos_segmentos["segmento_1"]} x {dados_dos_segmentos["segmento_2"]} x {dados_dos_segmentos["segmento_3"]}, {mensagem_de_retorno}.
''')


def main() -> None:
    system("clear")

    dados_dos_segmentos: dict = {
        "segmento_1": 0,
        "segmento_2": 0,
        "segmento_3": 0,
        "é_um_triângulo": False,
        "tipo_do_triângulo": ''
    }

    for x in range(1, 4):
        dados_dos_segmentos[f"segmento_{x}"] = obterSegmento(x)

    dados_dos_segmentos["é_um_triângulo"] = analisarSeFormaUmTriângulo(
        dados_dos_segmentos["segmento_1"], 
        dados_dos_segmentos["segmento_2"], 
        dados_dos_segmentos["segmento_3"]
    )

    if dados_dos_segmentos['é_um_triângulo']:
        dados_dos_segmentos["tipo_do_triângulo"] = definirQualTipoDeTriânguloÉ(
        dados_dos_segmentos["segmento_1"], 
        dados_dos_segmentos["segmento_2"], 
        dados_dos_segmentos["segmento_3"]
    )

    mostrarResultado(dados_dos_segmentos)


main()