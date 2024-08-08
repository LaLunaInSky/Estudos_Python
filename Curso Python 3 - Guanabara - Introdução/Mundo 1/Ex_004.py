#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ela.

print(f'\n{'- Escreva algo e te digo todas as informações sobre ele -':^62}\n')

palavraDigitada = str(input('Digite o que quiser: '))

print(f'\n- Foi digitado ({palavraDigitada}) -\n')

print(f'''O tipo primitivo é {type(palavraDigitada)}
Só tem espaços? {palavraDigitada.isspace()}
É um número? {palavraDigitada.isnumeric()}
É alfabético? {palavraDigitada.isalpha()}
É alfanúmerico? {palavraDigitada.isalnum()}
Está em maiúscula? {palavraDigitada.isupper()}
Está em minúscula? {palavraDigitada.islower()}
Está capitalizada? {palavraDigitada.istitle()}
''')