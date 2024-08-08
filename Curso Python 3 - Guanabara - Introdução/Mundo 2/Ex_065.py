#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valor lido. 
#O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

print(f'\n{'- Me informe vários números inteiros, e eu te devolvo algumas informações sobre os mesmos -':^96}\n')

númeroInformado = 0
númerosInformados = []
perguntaSobreContinuar = ''

while True:
    if perguntaSobreContinuar in '':
        perguntaSobreContinuar = 's'

    if perguntaSobreContinuar in 's':
        númeroInformado = int(input('\nDigite um valor: '))
        númerosInformados.append(númeroInformado)
        perguntaSobreContinuar = ''

    if perguntaSobreContinuar not in ['s', 'n']:
        perguntaSobreContinuar = str(input('Quer digitar um novo valor(S/N)? ')).strip().lower()
    elif perguntaSobreContinuar in 'n':
        break

somaDosNúmerosInformados = menorNúmeroInformado = maiorNúmeroInformado = 0

for contagem in range(0, len(númerosInformados)):
    somaDosNúmerosInformados += númerosInformados[contagem]

    if menorNúmeroInformado == 0  and maiorNúmeroInformado == 0:
        maiorNúmeroInformado = menorNúmeroInformado = númerosInformados[0]

    elif númerosInformados[contagem] < menorNúmeroInformado:
        menorNúmeroInformado = númerosInformados[contagem]
    
    elif númerosInformados[contagem] > maiorNúmeroInformado:
        maiorNúmeroInformado = númerosInformados[contagem]

print(f'\nA média dos {len(númerosInformados)} valores digitados é de {somaDosNúmerosInformados / len(númerosInformados)}, o menor número digitado foi {menorNúmeroInformado} e o maior foi {maiorNúmeroInformado}.\n')