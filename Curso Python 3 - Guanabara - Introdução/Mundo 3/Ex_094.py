#Crie um programa que leia nome, genêro e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
#A)Quantas pessoas foram cadastradas; B)A média das idades; C)Uma lista com todas as mulheres; D)Uma lista de pessoa com idade acima da média.

print(f'\n{'- Me informe o nome, genêro e idade de várias pessoas, e eu te devolvo algumas informações -':^97}\n')

dadosDasPessoas = []
quantidadeDePessoas = 1

while True:
    while quantidadeDePessoas != len(dadosDasPessoas):
        if quantidadeDePessoas > 1:
            print()

        dadoDaPessoa = {}

        dadoDaPessoa['nome'] = input(f'Qual o nome da {quantidadeDePessoas}ª pessoa? ').strip().capitalize()

        while True:
            dadoDaPessoa['genêro'] = input(f'Qual o genêro de {dadoDaPessoa["nome"]} (M/H)? ').strip().lower()

            if dadoDaPessoa['genêro'] in ('m', 'h'):
                break
            else:
                del dadoDaPessoa['genêro']
                print('\033[31mAPENAS É ACEITO M (mulher) OU H (homem)!\033[m\n')

        dadoDaPessoa['idade'] = int(input(f'Qual a idade de {dadoDaPessoa["nome"]}? '))

        dadosDasPessoas.append(dadoDaPessoa.copy())

        dadoDaPessoa.clear()

    perguntaSobreContinuar = input('\nQuer acrescentar mais uma pessoa(S/N)? ').strip().lower()

    if perguntaSobreContinuar in ('s', 'n'):
        if perguntaSobreContinuar == 'n':
            print()
            break
        else:
            quantidadeDePessoas += 1

    else:
        print('\033[31mAPENAS É ACEITO S (sim) OU N (não)!\033[m')

somaDasIdades = 0
mulheresCadastradas = []
pessoasComIdadeAcimaDaMédia = []

for pessoa in dadosDasPessoas:
    for key, value in pessoa.items():
        if key == 'idade':
            somaDasIdades += value
        
    if pessoa["genêro"] == 'm':
        mulheresCadastradas.append(pessoa["nome"])

for pessoa in dadosDasPessoas:
    if pessoa["idade"] >= (somaDasIdades / len(dadosDasPessoas)):
        pessoasComIdadeAcimaDaMédia.append(pessoa)

print(f'''{'-='*16}
Foram cadastradas {len(dadosDasPessoas)} pessoas.
A média de idade dos cadastrados é de {somaDasIdades / len(dadosDasPessoas):.1f} anos.
As mulheres cadastradas são:''', end=' ')

for posição, nome in enumerate(mulheresCadastradas):
    if len(mulheresCadastradas) == 1:
        print(f'{nome}.')
        
    else:
        if posição == 0:
            print(f'{nome}', end='')

        elif posição == (len(mulheresCadastradas) - 1):
            print(f' e {nome}.')

        else:
            print(f', {nome}', end='') 

print('As pessoas que possuem a idade acima da média são:')

for item in pessoasComIdadeAcimaDaMédia:
    print(item, end=' ')

print(f'\n{'-='*16}\n')