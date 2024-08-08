#Reescreva a função leiaInt() que fizemos no Ex_104, incluindo agora a possibilidade da digitação de um número do tipo inválido. 
#Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

#Ex_104: Crie um programa que tenha a função leiaInteiro(), que vai funcionar de forma semelhante à função input() do Python, só que fazendo a validação para aceitar 
#apenas um valor numérico.

import operações

númeroInteiro = operações.leiaInt(
    '\nInforme um número inteiro: '
)

númeroReal = operações.leiaFloat(
    'Informe um número Real: '
)

print(f'\nFoi informado o número Inteiro {númeroInteiro} e o número Real {númeroReal}.\n')