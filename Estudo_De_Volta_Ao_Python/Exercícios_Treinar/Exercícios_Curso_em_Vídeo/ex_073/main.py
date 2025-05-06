from os import system

def obterListaDosVintePrimeirosColocadosDoCampeonatoBrasileiroDeFutebolDeDoisMilEVinteEQuatro() -> list:
    vinte_primeiros_colocados_do_campeonato_brasileiro_de_futebol_de_2024: list = [
        "Botafogo", "Palmeiras", "Flamengo", "Fortaleza", "Internacional", "São Paulo", "Corinthians", "Bahia", "Cruzeiro", "Vasco da Gama", "Vitória", "Atlético Mineiro", "Fluminense", "Grêmio", "Juventude", "Red Bull Bragantino", "Athletico Paranaense", "Criciúma", "Atlético Goianiense", "Cuiabá"
    ]

    return vinte_primeiros_colocados_do_campeonato_brasileiro_de_futebol_de_2024


def analisarQuaisForamOsCincoPrimeirosColocados(lista_de_colocados: list) -> list:
    cinco_primeiros_colocados: list = []
    
    for contagem in range(0, 5):
        cinco_primeiros_colocados.append(lista_de_colocados[contagem])

    return cinco_primeiros_colocados


def analisarOsÚltimosQuatroColocados(lista_de_colocados: list) -> list:
    últimos_quatro_colocados: list = []

    for contagem in range((len(lista_de_colocados) - 4), len(lista_de_colocados)):
        últimos_quatro_colocados.append(lista_de_colocados[contagem])

    return últimos_quatro_colocados


def mostrarInformaçõesSobreATabelaDoCampeonatoBrasileiroDeFutebolDeDoisMilEVinteEQuatro(lista_de_colocados: list) -> None:
    print(f'''
Os 5 primeiros colocados foram: {analisarQuaisForamOsCincoPrimeirosColocados(lista_de_colocados)}.
Os Último 4 colocados são: {analisarOsÚltimosQuatroColocados(lista_de_colocados)}.''')
    
    lista_de_colocados.sort()
    
    print(f'''Os Times em Ordem Alfabética: {lista_de_colocados}.
A Chapecoense Não participou deste campeonato!
''')


def main() -> None:
    system("clear")

    vinte_primeiros_colocados_do_campeonato_brasileiro_de_futebol_de_2024: list = obterListaDosVintePrimeirosColocadosDoCampeonatoBrasileiroDeFutebolDeDoisMilEVinteEQuatro()

    mostrarInformaçõesSobreATabelaDoCampeonatoBrasileiroDeFutebolDeDoisMilEVinteEQuatro(vinte_primeiros_colocados_do_campeonato_brasileiro_de_futebol_de_2024)


main()