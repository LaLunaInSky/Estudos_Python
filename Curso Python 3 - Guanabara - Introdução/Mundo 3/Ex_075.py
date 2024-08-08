#Desenvolva um pograma que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#A)Quantas vezes apareceu o valor 9; B)Em que posição foi digitado o primeiro valor 3; C)Quais foram os números pares.

print(f'\n{'- Me informe 4 números inteiros, e eu te devolvo algumas informações sobre os mesmos -':^91}\n')

quantidadeDe9 = 0

númerosInformados = (
    int(input('Qual o 1º Número? ')), int(input('Qual o 2º Número? ')), int(input('Qual o 3º Número? ')), int(input('Qual o 4º Número? '))
)

print(f'\nO número (9) apareceu {númerosInformados.count(9)} vezes. O número (3) apareceu pela primeira vez', end=' ')

if númerosInformados.count(3) == 0:
    print('em nenhuma posição.', end=' ')
else:
    print(f'na {númerosInformados.index(3) + 1}ª posição.', end=' ')

print('Os números pares foram:', end=' ')

for números in númerosInformados:
    if números % 2 == 0:
        print(números, end='.. ')

print('\n\n')