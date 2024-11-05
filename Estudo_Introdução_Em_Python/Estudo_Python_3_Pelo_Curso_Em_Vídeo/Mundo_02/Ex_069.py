#Crie um programa que leia a idade e o genêro de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. 
#No final mostre: A)quantas pessoas tem mais de 18 anos; B)quantos homens foram cadastrados; C)quantas mulheres tem menos de 20 anos.

print(f'\n{'- Me informe a idade e o genêro de algumas pessoas, e eu te devolvo algumas informações sobre os mesmos -':^110}\n')

perguntaSobreContinuar = ''
quantidadeDePessoasInformadas = 1
quantidadeDeMaioresDeIdade = quantidadeDeHomens = quantidadeDeMulheresAbaixoDe20Anos = 0

while perguntaSobreContinuar != 'n':
    print(f'\n{f' {quantidadeDePessoasInformadas}ª Pessoa ':-^40}')
    idadeDaPessoa = int(input('Qual a idade? '))

    if idadeDaPessoa >= 18:
        quantidadeDeMaioresDeIdade += 1

    while True:
        genêroDaPessoa = input('Qual o genêro(H/M)? ').strip().lower()[0]

        if genêroDaPessoa not in ['h', 'm']:
            print('\033[31mAPENAS É ACEITO H (homem) OU M (mulher)!\033[m\n')
        else:
            break

    if genêroDaPessoa == 'h':
        quantidadeDeHomens += 1

    if idadeDaPessoa < 20 and genêroDaPessoa == 'm':
        quantidadeDeMulheresAbaixoDe20Anos += 1

    while True:
        perguntaSobreContinuar = input('\nQuer acrescentar mais um dado de outra pessoa(S/N)? ').strip().lower()[0]

        if perguntaSobreContinuar == 's':
            quantidadeDePessoasInformadas += 1

        if perguntaSobreContinuar not in ['s', 'n']:
            print('\033[31mAPENAS É ACEITO S (sim) OU N (não)!\033[m\n')
        else:
            break

pluralDeHomens = 'm'
pluralDeMulheres = pluralDeCadastros = ''
pluralDeForam = 'i'

if quantidadeDeHomens != 1:
    pluralDeHomens = 'ns'
    pluralDeForam = 'ram'
    pluralDeCadastros = 's'

if quantidadeDeMulheresAbaixoDe20Anos != 1:
    pluralDeMulheres = 'es'

print(f'\nDe todas as pessoas cadastradas apenas {quantidadeDeMaioresDeIdade} é maior de idade, {quantidadeDeHomens} home{pluralDeHomens} fo{pluralDeForam} cadastrado{pluralDeCadastros}, e tem {quantidadeDeMulheresAbaixoDe20Anos} mulher{pluralDeMulheres} com menos de 20 anos.\n')