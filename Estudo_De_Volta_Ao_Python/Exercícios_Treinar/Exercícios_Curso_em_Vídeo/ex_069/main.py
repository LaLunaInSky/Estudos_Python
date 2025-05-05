from os import system

def mostrarFraseDoCadastro(número_do_cadastro: int = 1) -> None:
    print(f"{"-" * 25}\n{f"Cadastro da {número_do_cadastro}ª Pessoa":^25}\n{"-" * 25}")


def obterAIdadeDaPessoa() -> int:
    idade_da_pessoa: int = int(input("Qual a idade? "))

    return idade_da_pessoa


def obterOGêneroDaPessoa(número_do_cadastro: int, idade_da_pessoa: int) -> str:
    while True:
        gênero_da_pessoa: str = str(input("Qual o gênero [M/F]? ")).lower()

        if gênero_da_pessoa == 'f' or gênero_da_pessoa == 'm':
            return gênero_da_pessoa
        else:
            system("clear")

            mostrarFraseDoCadastro(número_do_cadastro)
            print(f"Qual a idade? {idade_da_pessoa}")


def perguntarSeQuerAdicionarMaisUmaPessoa(número_do_cadastro: int, idade_da_pessoa: int, gênero_da_pessoa: str) -> str:
    while True:
        pergunta_se_quer_adicionar_mais_uma_pessoa: str = str(input("\nQuer Adicionar mais uma Pessoa [S/N]? ")).lower()

        if pergunta_se_quer_adicionar_mais_uma_pessoa == 's' or pergunta_se_quer_adicionar_mais_uma_pessoa == 'n':
            return pergunta_se_quer_adicionar_mais_uma_pessoa
        
        else:
            system("clear")

            mostrarFraseDoCadastro(número_do_cadastro)
            print(f"Qual a idade? {idade_da_pessoa}")
            print(f"Qual o gênero [M/F]? {gênero_da_pessoa}")


def organizadorDaEntradaDeCadastroDasPessoas() -> list:
    pessoas_cadastradas: list = []

    while True:
        mostrarFraseDoCadastro(len(pessoas_cadastradas) + 1)
        
        idade_da_pessoa: int = obterAIdadeDaPessoa()
        gênero_da_pessoa: str = obterOGêneroDaPessoa(len(pessoas_cadastradas) + 1, idade_da_pessoa)

        pessoas_cadastradas.append((idade_da_pessoa, gênero_da_pessoa))

        resposta_se_quer_adicionar_mais_uma_pessoa: str = perguntarSeQuerAdicionarMaisUmaPessoa(len(pessoas_cadastradas), pessoas_cadastradas[-1][0], pessoas_cadastradas[-1][1])

        if resposta_se_quer_adicionar_mais_uma_pessoa == 's':
            system("clear")

        elif resposta_se_quer_adicionar_mais_uma_pessoa == 'n':
            return pessoas_cadastradas


def analisarQuantasPessoasTemMaisDeDezoitoAnos(pessoas_cadastradas: list) -> int:
    quantidade_de_pessoas_com_mais_de_dezoito_anos: int = 0

    for pessoa in pessoas_cadastradas:
        if pessoa[0] > 18:
            quantidade_de_pessoas_com_mais_de_dezoito_anos += 1

    return quantidade_de_pessoas_com_mais_de_dezoito_anos


def analisarQuantosHomensForamCadastrados(pessoas_cadastradas: list) -> int:
    quantidade_de_homens_cadastrados: int  = 0

    for pessoa in pessoas_cadastradas:
        if pessoa[1] == 'm':
            quantidade_de_homens_cadastrados += 1

    return quantidade_de_homens_cadastrados


def analisarQuantasMulheresTemMenosDeVinteAnos(pessoas_cadastradas: list) -> int:
    quantidade_de_mulheres_com_menos_de_vinte_anos: int = 0

    for pessoa in pessoas_cadastradas:
        if pessoa[1] == 'f' and pessoa[0] < 20:
            quantidade_de_mulheres_com_menos_de_vinte_anos += 1

    return quantidade_de_mulheres_com_menos_de_vinte_anos


def mostrarInformaçõesDasPessoasCadastradas(pessoas_cadastradas: list) -> None:
    system("clear")

    print(f'''
Nas pessoas castradas existem {analisarQuantasPessoasTemMaisDeDezoitoAnos(pessoas_cadastradas)} com mais de 18 anos,
foram cadastrados {analisarQuantosHomensForamCadastrados(pessoas_cadastradas)} homens,
e possui {analisarQuantasMulheresTemMenosDeVinteAnos(pessoas_cadastradas)} mulheres com menos de 20 anos.
''')


def main() -> None:
    system("clear")

    pessoas_cadastradas: list = organizadorDaEntradaDeCadastroDasPessoas()
    
    mostrarInformaçõesDasPessoasCadastradas(pessoas_cadastradas)


main()