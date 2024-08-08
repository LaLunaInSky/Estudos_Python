from utilidadesCeV import moedas

def aumentar(preço, taxa, mostrarMoeda=False):
    resultado = preço + (preço * taxa / 100)
    return moedas.mostradorMoeda(resultado, mostrarMoeda)


def diminuir(preço, taxa, mostrarMoeda=False):
    resultado = preço - (preço * taxa / 100)
    return moedas.mostradorMoeda(resultado, mostrarMoeda)


def dobrar(preço, mostrarMoeda=False):
    resultado = preço * 2
    return moedas.mostradorMoeda(resultado, mostrarMoeda)


def dividir(preço, mostrarMoeda=False):
    resultado = preço / 2
    return moedas.mostradorMoeda(resultado, mostrarMoeda)


def resumo(preço=0, taxaAumentar=10, taxaDiminuir=5, mostrarMoeda=True):
    print(f'''
{'-' * 40}\n{f' Resultado do Preço {moedas.moeda(preço)} ':^40}\n{'-' * 40}
{'→ O Dobro':.<20}{dobrar(preço, True):.>20}
{'→ A Metade':.<20}{dividir(preço, True):.>20}
{f'→ Aumento de {taxaAumentar}%':.<20}{aumentar(preço, taxaAumentar, True):.>20}
{f'→ Desconto de {taxaDiminuir}%':.<20}{diminuir(preço, taxaDiminuir, True):.>20}
{'-' * 40}
''')