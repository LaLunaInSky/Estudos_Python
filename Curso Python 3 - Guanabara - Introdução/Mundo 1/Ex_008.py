#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

print(f'\n{'- Informe um valor em metros, e eu te devolvo o mesmo em km, hm, dam, dm, cm, mm -':^87}\n')

valorEmMetros = float(input('Qual o valor em metros? '))

print(f'\n{valorEmMetros/1000}km -> {valorEmMetros/100}hm -> {valorEmMetros/10}dam -> {valorEmMetros}m <- {valorEmMetros*10}dm <- {valorEmMetros*100}cm <- {valorEmMetros*1000}mm\n')