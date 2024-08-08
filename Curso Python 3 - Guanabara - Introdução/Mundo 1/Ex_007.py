#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

print(f'\n{'- Informe duas notas, e eu te devolvo a média -':^52}\n')

primeiraNota = float(input('Qual a 1ª nota? '))

segundaNota = float(input('Qual a 2ª nota? '))

print(f'\nA média das notas {primeiraNota:.1f} e {segundaNota:.1f} é igual a {(primeiraNota+segundaNota)/2:.1f} \n')