def mostarMenu():
    print(f'''
{'-' * 40}\n{' MENU PRINCIPAL ':^40}\n{'-' * 40}
1 - Cadastrar Novo Usuário
2 - Ver a Listagem Dos Usuários
3 - Fechar o Programa
{'-' * 40}''')


def menu(nomeDoArquivo='dados_pessoas.txt'):
    from time import sleep

    nomeArquivo = f'e:\Documentos\Estudo De Programação\Python\Curso Python 3 - Guanabara - Introdução\Mundo 3\Ex_115\{nomeDoArquivo}'

    mostarMenu()

    while True:
        try:
            opçãoInformada = int(input('Qual a opção do menu? '))

        except:
            print('\033[41mApenas é aceito as opções do menu!\033[m\n')
            sleep(2)
            mostarMenu()
        
        else:
            if opçãoInformada < 1 or opçãoInformada > 3:
                print('\033[41mApenas é aceito as opções do menu!\033[m\n')
                sleep(2)

            elif opçãoInformada == 3:
                sleep(0.5)
                print(f'\n- FECHANDO O PROGRAMA -\n')
                sleep(1)
                break

            elif opçãoInformada == 1:
                sleep(1)
                cadastroPessoa(nomeArquivo)
                sleep(2)
            
            else:
                sleep(1)
                listagemPessoas(nomeArquivo)
                sleep(3)

            mostarMenu()


def cadastroPessoa(nomeArquivo):
    print(f'\n{'-' * 40}\n{' NOVO CADASTRO ':^40}\n{'-'*40}')
    while True:
        nome = str(input('Qual o nome? ')).strip().title()

        if nome.isalpha():
            break
        
        else:
           print('\033[31mAPENAS É ACEITO NOME VÁLIDO!\033[m')

    while True:
        try:
            idade = int(input(f'Qual a idade de {nome}? '))

        except:
            print('\033[31mAPENAS É ACEITO NÚMEROS!\033[m')

        else:
            break
    
    try:
        with open(nomeArquivo, 'r') as arquivo:
            pass

    except:
        with open(nomeArquivo, 'w') as arquivo:
            arquivo.write(f'{nome}, {idade} anos')
            
    else:
        with open(nomeArquivo, 'a') as arquivo:
            arquivo.write(f'\n{nome}, {idade} anos')

    print(f'{'-'*40}')


def listagemPessoas(nomeArquivo):
    try:
        with open(nomeArquivo, 'r') as arquivo:
            pass
    
    except:
        return print('\033[41mERRO! Nenhuma lista encontrada! Tente cadastrar alguma pessoa...\033[m')
    
    else:
        print(f'\n{'-' * 40}\n{' PESSOAS CADASTRADAS ':^40}\n{'-' * 40}')

        with open(nomeArquivo, 'r') as arquivo:
            pessoas = arquivo.readlines()
            dados = {}
        
            for contagem in range(0, len(pessoas)):
                dados[f'{contagem+1}º pessoa'] = pessoas[contagem].replace('\n', '').split(', ')

            for value in dados.values():
                print(f' {value[0]:<29}{value[1]:>9} ')