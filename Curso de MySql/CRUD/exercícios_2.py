import mysql.connector

resultado_final = {}

conexão = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='cadastro'
)

cursor = conexão.cursor()


# 1º Exercício - Uma lista com as profissões dos gafanhotos e seus respectivos quantitativos
cursor.execute(
    'select `profissao`, count(*) from `gafanhotos` group by `profissao` order by `profissao`'
)
resultado_final['1º Exercício'] = cursor.fetchall()


# 2º Exercício - Quantos gafanhotos homens e quantas mulheres nasceram após 01.01.2005
cursor.execute(
    'select `gênero`, count(*) from `gafanhotos` where nascimento > "2005-01-01" group by `gênero`'
)
resultado_final['2º Exercício'] = cursor.fetchall()


# 3º Exercício - Uma lista com os gafanhotos que nasceram fora do Brasil, mostrado o país de origem e o total de pessoas nascidas lá. Só nos interessam os países que tiverem mais de 3 gafanhotos com nacionalidade
cursor.execute(
    'select `nacionalidade`, count(*) from `gafanhotos` where nacionalidade != "Brasil" group by `nacionalidade` having count(*) > 3 order by `nacionalidade`'
)
resultado_final['3º Exercício'] = cursor.fetchall()


# 4º Exercício - Uma lista agrupada pela altura dos gafanhotos, mostrando quantas pessoas pesam mais de 100kg e que estão acima da média de altura de todos os cadastrados
cursor.execute(
    'select `altura`, count(*) from `gafanhotos` where `peso` > 100 and `altura` > (select avg(`altura`) from `gafanhotos`) group by `altura`'
)
resultado_final['4º Exercício'] = cursor.fetchall()


cursor.close()
conexão.close()

for key, value in resultado_final.items():
    print(f'\n{'-' * 10} {key} {'-' * 10}')
    for c in range(0, len(value)):
        if len(value) == 1:
            print(value[c][0])
        else:
            print(value[c])