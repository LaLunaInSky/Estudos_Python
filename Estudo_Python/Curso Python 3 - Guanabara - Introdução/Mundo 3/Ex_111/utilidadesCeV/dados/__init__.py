from utilidadesCeV import moedas

def resumo(preço=0, taxaAumento=10, taxaDiminui= 5):
    print(f'''
{'-' * 40}\n{f' RESULTADO DO PREÇO {moedas.moeda(preço)} ':^40}\n{'-' * 40}
{'→ O Dobro':.<20}{dobrar(preço, True):.>20}
{'→ A Metade':.<20}{metade(preço, True):.>20}
{f'→ Aumento de {taxaAumento}%':.<20}{aumentar(preço, taxaAumento, True):.>20}
{f'→ Desconto de {taxaDiminui}%':.<20}{diminuir(preço, taxaDiminui, True):.>20}
{'-' * 40}
''')

def aumentar(preço , taxa, mostrarMoeda=False):
    resultado = preço + (preço * taxa / 100)
    return moedas.mostradorMoeda(resultado, mostrarMoeda)


def diminuir(preço, taxa, mostrarMoeda=False):
    resultado = preço - (preço * taxa / 100)
    return moedas.mostradorMoeda(resultado, mostrarMoeda)


def dobrar(preço, mostrarMoeda=False):
    resultado = preço * 2
    return moedas.mostradorMoeda(resultado, mostrarMoeda)


def metade(preço, mostrarMoeda=False):
    resultado = preço / 2
    return moedas.mostradorMoeda(resultado, mostrarMoeda)