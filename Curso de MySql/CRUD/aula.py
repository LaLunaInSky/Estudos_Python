import mysql.connector

resultado_final = {}

conexão = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='cadastro'
)
cursor = conexão.cursor()


# 1º Execício - Uma lista com o nome de todas as gafanhotas
cursor.execute(
    'select `nome` from `gafanhotos` where `gênero` = "F" order by `nome`'
)
resultado_final['1º Exercício'] = cursor.fetchall()


# 2º Execício - Uma lista com os dados de todos aqueles que nasceram ente 1.01.2000 e 31.12.2015
cursor.execute(
    'select * from `gafanhotos` where `nascimento` between "2000-01-01" and "2015-12-31" order by `nascimento`'
)
resultado_final['2º Exercício'] = cursor.fetchall()


# 3º Execício - Uma lista com o nome de todos os homens que trabalham como programadores
cursor.execute(
    'select `nome` from `gafanhotos` where `profissao` = "Programador" and `gênero` = "M" order by `nome`'
)
resultado_final['3º Exercício'] = cursor.fetchall()


# 4º Execício - Uma lista com os dados de todas as mulheres que nasceram no Brasil e que têm seu nome iniciando com a letra J
cursor.execute(
    'select * from `gafanhotos` where `gênero` = "F" and `nacionalidade` = "Brasil" and `nome` like "j%" order by `nome`'
)
resultado_final['4º Exercício'] = cursor.fetchall()


# 5º Execício - Uma lista com o nome e a nacionalidade de todos os homens que têm Silva no nome, não nasceram no Brasil e pesam menos de 100kg
cursor.execute(
    'select `nome`, `nacionalidade` from `gafanhotos` where `gênero` = "M" and `nome` like "%Silva" and `nacionalidade` != "Brasil" and `peso` < 100 order by `nome`'
)
resultado_final['5º Exercício'] = cursor.fetchall()


# 6º Execício - Qual é a maior altura entre gafanhotos homens que moram no Brasil
cursor.execute(
    'select max(`altura`) from `gafanhotos` where `gênero` = "M" and `nacionalidade` = "Brasil"'
)
resultado_final['6º Exercício'] = cursor.fetchall()


# 7º Execício - Qual é a média de peso dos gafanhotos cadastrados
cursor.execute(
    'select avg(`peso`) from `gafanhotos`'
)
resultado_final['7º Exercício'] = cursor.fetchall()


# 8º Execício - Qual é o menor peso entre as gafanhotos mulheres que nasceram fora do Brasil e entre 1.01.1990 e 31.12.2000
cursor.execute(
    'select min(`peso`) from `gafanhotos` where `gênero` = "F" and `nacionalidade` != "Brasil" and nascimento between "1999-01-01" and "2000-12-31"'
)
resultado_final['8º Exercício'] = cursor.fetchall()


# 9º Execício - Quantos gafanhotos mulheres têm mais de 1.90m de altura
cursor.execute(
    'select * from `gafanhotos` where `gênero` = "F" and `altura` > "1.90" order by `nome`'
)
resultado_final['9º Exercício'] = cursor.fetchall()


cursor.close()
conexão.close()

for key, value in resultado_final.items():
    print(f'\n{'-'*10} {key} {'-'*10}')
    for c in range(0, len(value)):
        print(value[c])
