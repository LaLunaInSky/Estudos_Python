#Crie um pacote chamdao utilidadesCeV que tenha dois módulos interno chamados moeda e dado. Transfira todas as funções utilizadas no 
#Ex_107, Ex_108 e Ex_109 para o primeiro pacote e mantenha tudo funcionando.

from utilidadesCeV import dados

preçoInformado = float(input('\nQual o preço? R$'))

dados.resumo(preçoInformado)