#Crie uma tupla preenchida com os 20 primeiro colocados da Tabela do Compeonato Brasileiro de Futebol, na ordem de colocação.
#Depois mostre: A)Os 5 primeiros; B)Os últimos 4 colocados; C)Times em ordem alfabética; D)Em que posição está o time da Chapecoense.

print(f'\n{'- Tabela Da Final Do Campeonato Brasileiro De Futebol de 2023, e algumas informações -':^91}\n')

timesFinaisDoCampeonatoBrasileiroDeFutebolDe2023 = ('Palmeiras', 'Grêmio', 'Atlético', 'Flamengo', 'Botafogo', 'Bragantino', 'Fluminense', 'Athletico-PR', 'Internacional', 
'Fortaleza', 'São Paulo', 'Cuiabá', 'Corinthians', 'Cruzeiro', 'Vasco', 'Bahia', 'Santos', 'Goiás', 'Coritiba', 'América')

for posição, nomeDoTime in enumerate(timesFinaisDoCampeonatoBrasileiroDeFutebolDe2023):
    print(f'{posição + 1}ª → {nomeDoTime}')

print('\nOs 5 primeiros colocados foram:')

for contagem in range(0, 5):
    if contagem == 4:
        print(timesFinaisDoCampeonatoBrasileiroDeFutebolDe2023[contagem], '\n')
    else:
        print(timesFinaisDoCampeonatoBrasileiroDeFutebolDe2023[contagem], end=' → ')

print('Os 4 últimos colocados foram:')

for nomeDoTime in timesFinaisDoCampeonatoBrasileiroDeFutebolDe2023[-4:]:
    if nomeDoTime == timesFinaisDoCampeonatoBrasileiroDeFutebolDe2023[-1]:
        print(nomeDoTime, '\n')
    else:
        print(nomeDoTime, end=' → ')

print('Os times em ordem Alfabétia:')

for posiçãoDoTime, nomeDoTime in enumerate(sorted(timesFinaisDoCampeonatoBrasileiroDeFutebolDe2023)):
    if posiçãoDoTime in [4, 9, 14, 19]:
        print(nomeDoTime)
    else:
        print(nomeDoTime, end=' → ')

print('\nO time Chapecoense está', end=' ')

if timesFinaisDoCampeonatoBrasileiroDeFutebolDe2023.count('Chapecoense') == 0:
    print('em nenhuma posição esse ano.\n')
else:
    print(f'na {timesFinaisDoCampeonatoBrasileiroDeFutebolDe2023.index('chapecoense') + 1}ª posição.\n')