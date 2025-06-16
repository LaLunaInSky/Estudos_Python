#Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses 
#abertos e fechados na ordem correta.

print(f'\n{'- Me informe um expressão matemática com parênteses, e eu te digo se ela é possivel -':^90}\n')

operaçãoMatemática = [input('Escreva a operação com Parênteses: ')]

contagemDeParêntesesEsquerda = contagemDeParêntesesDireita = 0

for item in operaçãoMatemática[0]:
    if item == '(':
        contagemDeParêntesesEsquerda += 1
    elif item == ')':
        contagemDeParêntesesDireita += 1

print(f'\nA operação matemática com parênteses {operaçãoMatemática[0]},', end=' ')

if contagemDeParêntesesEsquerda == contagemDeParêntesesDireita:
    print('é possível!\n')
else:
    print('não é possível!\n')