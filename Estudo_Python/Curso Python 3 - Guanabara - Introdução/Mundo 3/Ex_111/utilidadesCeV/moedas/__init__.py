def moeda(preço, moeda='R$'):
    resultado = f'{moeda}{preço:.2f}'.replace('.', ',')
    return resultado


def mostradorMoeda(resultado, aparecerMoeda=False):
    if aparecerMoeda == True:
        return moeda(resultado)
    else:
        return resultado