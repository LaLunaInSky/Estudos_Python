#Refaça o Ex_009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

print(f'\n{'- Me informe um número qualquer, e eu te devolvo sua tabuada -':^67}\n')

númeroEscolhido = int(input('Qual número você escolhe? '))

print(f'\nA Tabuada do {númeroEscolhido} é:')

for contagem in range(1, 11):
    print(f'{númeroEscolhido} X {contagem:2} = {númeroEscolhido * contagem}')
print()