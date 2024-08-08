#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
#Ex: Ana Maria de Souza
#Primeiro = Ana
#Último = Souza

print(f'\n{'- Me informe seu nome completo, e eu te digo seu primeiro e último nome -':^78}\n')

nomeCompleto = input('Qual o seu nome completo? ').strip()

print(f'''
Prazer em te conhecer, {nomeCompleto.title()}.
Seu primeiro nome é: {nomeCompleto.split()[0].capitalize()}
Seu último nome é: {nomeCompleto.split()[-1].capitalize()}
''')