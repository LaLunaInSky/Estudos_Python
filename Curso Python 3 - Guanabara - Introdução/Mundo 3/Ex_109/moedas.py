def aumentar(preço, taxa, mostrarMoeda=False):
    resultado = preço + (preço * taxa / 100)
    if mostrarMoeda == True:
        return moeda(resultado)
    else:
        return resultado


def diminuir(preço, taxa, mostrarMoeda=False):
    resultado = preço - (preço * taxa / 100)
    if mostrarMoeda == True:
        return moeda(resultado)
    else:
        return resultado


def dobro(preço, mostrarMoeda=False):
    resultado = preço * 2
    if mostrarMoeda == True:
        return moeda(resultado)
    else:
        return resultado


def metade(preço, mostrarMoeda=False):
    resultado = preço / 2
    if mostrarMoeda == True:
        return moeda(resultado)
    else:
        return resultado


def moeda(preço, moeda='R$'):
    resultado = f'{moeda}{preço:.2f}'.replace('.', ',')
    return resultado