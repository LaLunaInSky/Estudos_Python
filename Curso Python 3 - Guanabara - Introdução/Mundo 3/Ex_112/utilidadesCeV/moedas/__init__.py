def moeda(preço, moeda='R$'):
    resultado = f'{moeda}{preço:.2f}'.replace('.', ',')
    return resultado


def mostradorMoeda(resultado, aparecerMoeda=False):
    if aparecerMoeda == True:
        return moeda(resultado)
    else:
        return resultado


def leiaDinheiro(texto):

    def erro():
        print('\033[41mAPENAS É ACEITO NÚMEROS!\033[m')

    while True:
        preço = input(texto).strip().replace(',', '.')

        if '.' in preço:
            resultadoSemOArgumento = preço.replace('.', '')

            if resultadoSemOArgumento.isnumeric():
                return float(preço)
                break

            else:
                erro()
        
        elif preço.isnumeric():
            return float(preço)
            break

        else:
            erro()