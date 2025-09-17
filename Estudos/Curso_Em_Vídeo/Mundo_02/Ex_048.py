#Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.

print(f'\n{'- Irei te mostrar a soma dos números múltiplos por 3 na sequência -':^72}\n')

quantidadeDeÍmpares = 0
somaDosNúmerosÍmpares = 0

for númeroÍmpar in range(1, 500, 2):
    if númeroÍmpar % 3 == 0:
        quantidadeDeÍmpares += 1
        somaDosNúmerosÍmpares += númeroÍmpar

print(f'Foram {quantidadeDeÍmpares} números ímpares múltiplos por 3 achados na sequência. Somando tudo o resultado é de {somaDosNúmerosÍmpares}.\n')