from os import system

def obterQuantidadeDeDiasAlugadosDoCarro():
    dias_alugados_do_carro = int(input("Quantos dias você ficou com o carro? "))
    return dias_alugados_do_carro


def calcularValorDosDiasAlugadosDoCarro(dias_alugados):
    return round(float((dias_alugados * 60)), 2)


def obterQuantidadeDeKmRodadosComOCarro():
    kms_rodados_com_o_carro = round(float(input("Quantos Km você rodou com o carro? ")), 1)
    return kms_rodados_com_o_carro


def calcularValorDosKmsRodadosComOCarro(kms_rodados):
    return round(float(kms_rodados * 0.15), 1)


def calcularOValorTotalAPagar(valor_dias, valor_kms):
    return round((valor_dias + valor_kms), 2)


def mostrarResultado(dias_alugados, kms_rodados, valor_total):
    print(f"\nO carro alugado por {dias_alugados} dias e que percorreu {kms_rodados}Km, fica com o valor de R${valor_total}\n")


def main():
    system("clear")

    dias_alugados_do_carro = obterQuantidadeDeDiasAlugadosDoCarro()
    valor_a_pagar_pelos_dias_alugados_do_carro = calcularValorDosDiasAlugadosDoCarro(dias_alugados_do_carro)

    kms_rodados_com_o_carro = obterQuantidadeDeKmRodadosComOCarro()
    valor_a_pagar_pelos_kms_rodados_com_o_carro = calcularValorDosKmsRodadosComOCarro(kms_rodados_com_o_carro)

    total_a_pagar = calcularOValorTotalAPagar(valor_a_pagar_pelos_dias_alugados_do_carro, valor_a_pagar_pelos_kms_rodados_com_o_carro)

    mostrarResultado(dias_alugados_do_carro, kms_rodados_com_o_carro, total_a_pagar)


main()