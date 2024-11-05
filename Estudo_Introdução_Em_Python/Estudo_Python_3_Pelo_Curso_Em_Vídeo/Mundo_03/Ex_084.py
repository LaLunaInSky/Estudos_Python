#Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre: 
#A)Quantas pessoas foram cadastradas. B)Uma listagem com as pessoas mais pesadas. C)Uma listagem com as pessoas mais leves.

print(f'\n{'- Me informe o nome e o peso de várias pessoas, e eu te devolvo quais foram o menor e o maior peso -':^105}\n')

listaDasInformaçõesDasPessoas = []
listaDeDadoDaPessoa = []
quantidadeDePessoas = 1

while True:
    while quantidadeDePessoas != len(listaDasInformaçõesDasPessoas):
        listaDeDadoDaPessoa.append(input(f'Nome da {quantidadeDePessoas}ª pessoa: ').strip())
        listaDeDadoDaPessoa.append(float(input(f'Peso da {quantidadeDePessoas}ª Pessoa: ')))
        listaDasInformaçõesDasPessoas.append(listaDeDadoDaPessoa[:])
    
    listaDeDadoDaPessoa.clear()

    perguntaSobreContinuar = input('Quer acrescentar mais um dado(S/N)? ').strip().lower()

    if perguntaSobreContinuar in ('s', 'n'):
        if perguntaSobreContinuar == 'n':
            break
        else:
            quantidadeDePessoas += 1
            print()

    else:
        print('\033[31mAPENAS É ACEITO S (sim) OU N (não)!\033[m\n')

menorPeso = maiorPeso = 0

for posição, pessoa in enumerate(listaDasInformaçõesDasPessoas):
    if posição == 0:
        menorPeso = maiorPeso = pessoa[1]
    
    else:
        if pessoa[1] < menorPeso:
            menorPeso = pessoa[1]
        
        elif pessoa[1] > maiorPeso:
            maiorPeso = pessoa[1]

print(f'''
Foram cadastradas {len(listaDasInformaçõesDasPessoas)} pessoas.
O maior peso cadastrado foi {maiorPeso:.2f}kg:''', end=' ')

for pessoa in listaDasInformaçõesDasPessoas:
    if maiorPeso in pessoa:
        print(f'[{pessoa[0].title()}]', end=' ')

print(f'\nO menor peso cadastrado foi {menorPeso:.2f}Kg:', end=' ')

for pessoa in listaDasInformaçõesDasPessoas:
    if menorPeso in pessoa:
        print(f'[{pessoa[0].title()}]', end=' ')

print('\n')