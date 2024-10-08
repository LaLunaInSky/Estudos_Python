#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas e minúsculas.
#Quantas letras ao todo(sem considerar espaços).
#Quantas letras tem o primeiro nome.

print(f'\n{'- Me informe seu nome completo, e eu vou lhe devolvo algumas informações sobre o mesmo -':^93}\n')

nomeCompleto = input('Qual o seu nome completo? ').strip()

nomeSeparados = nomeCompleto.split()

print(f'''
O seu nome em letras maiúsculas fica: {nomeCompleto.upper()}
O seu nome em letras minúsculas fica: {nomeCompleto.lower()}
O seu nome possuí ao todo {len(nomeCompleto.replace(' ', ''))} letras.
O seu primeiro nome {nomeSeparados[0]} possuí {len(nomeSeparados[0])} letras.
''')