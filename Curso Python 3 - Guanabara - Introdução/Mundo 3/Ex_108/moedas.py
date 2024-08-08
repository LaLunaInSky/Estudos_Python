def aumentar(preço, taxa):
    resultado = preço + (preço * taxa / 100)
    return resultado


def diminuir(preço, taxa):
    resultado = preço - (preço * taxa / 100)
    return resultado


def dobro(preço):
    resultado = preço * 2
    return resultado


def metade(preço):
    resultado = preço / 2
    return resultado


def moeda(preço, moeda='R$'):
    resultado = f'{moeda}{preço:.2f}'.replace('.', ',')
    return resultado
