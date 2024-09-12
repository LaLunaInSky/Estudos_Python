def resumo(preço=0, taxaAumento=10, taxaDiminuir=5):
    print(f'''
{'-'*40}\n{f' RESULTADO DO PREÇO {moeda(preço)} ':^40}\n{'-'*40}
{'→ O Dobro':.<20}{f'{dobro(preço, True)}':.>20}
{'→ A Metade':.<20}{f'{metade(preço, True)}':.>20}
{f'→ Aumento de {taxaAumento}%':.<20}{f'{aumentar(preço, taxaAumento, True)}':.>20}
{f'→ Desconto de {taxaDiminuir}%':.<20}{f'{diminiur(preço, taxaDiminuir, True)}':.>20}
{'-'*40}
''')


def mostradorMoeda(resultado, aparecerMoeda=False):
    if aparecerMoeda == True:
        return moeda(resultado)
    else:
        return resultado


def aumentar(preço, taxa, mostrarMoeda=False):
    resultado = preço + (preço * taxa / 100)
    mostar = mostrarMoeda
    return mostradorMoeda(resultado, mostar)


def diminiur(preço, taxa, mostrarMoeda=False):
    resultado = preço - (preço * taxa / 100)
    mostar = mostrarMoeda
    return mostradorMoeda(resultado, mostar)


def dobro(preço, mostrarMoeda=False):
    resultado = preço * 2
    mostrar = mostrarMoeda
    return mostradorMoeda(resultado, mostrar)


def metade(preço, mostrarMoeda=False):
    resultado = preço / 2
    mostrar = mostrarMoeda
    return mostradorMoeda(resultado, mostrar)


def moeda(preço, moeda='R$'):
    resultado = f'{moeda}{preço:.2f}'.replace('.', ',')
    return resultado