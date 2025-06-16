from os import system

def obterNúmeroInteiro():
    input_user = int(input("Digite um número: "))
    return input_user


def mostrarTabuada(número_inteiro=1):
    print()
    for x in range(10):
        if x == 9 :
            print(f"{número_inteiro} X {x+1} = {número_inteiro * (x+1)}\n")    
        else:
            print(f"{número_inteiro} X  {x+1} = {número_inteiro * (x+1)}")


def main():
    system("clear")

    número_digitado = obterNúmeroInteiro()
    
    mostrarTabuada(número_digitado)


main()