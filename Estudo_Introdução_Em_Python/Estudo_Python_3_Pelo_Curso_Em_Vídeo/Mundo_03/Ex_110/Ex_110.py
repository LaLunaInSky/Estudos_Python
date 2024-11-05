#Adicione ao módulo moedas.py criado nos desafios anteriores, uma função chamada resumo(), que mostre na tela algumas informações geradas pelas 
#funções que já temos no módulo criado até aqui.

import moedas

moedas.resumo(
    float(input('\nQual o preço? R$')),
    int(input('Qual a taxa de Aumento? ')),
    int(input('Qaul a taxa de Desconto? '))
)