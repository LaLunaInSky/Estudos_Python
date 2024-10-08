def leiaInt(mensagem):
    while True:
        try:        
            númeroInteiro = int(input(mensagem))
        
        except:
            print('\033[31mErro! Apenas é aceito número INTEIRO!\033[m')

        else:
            return númeroInteiro
            break


def leiaFloat(mensagem):
    while True:
        try:
            númeroReal = float(input(mensagem))
        
        except:
            print('\033[31mErro! Apenas é aceito número REAL!\033[m\n')

        else:
            return númeroReal
            break