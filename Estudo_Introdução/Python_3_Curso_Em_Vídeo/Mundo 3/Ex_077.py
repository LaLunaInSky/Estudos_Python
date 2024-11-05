#Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

print(f'\n{'- Irei passar algumas informações sobre as palavras que aparecerem -':^73}\n')

palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')

for palavra in palavras:
    print(f'A palavra {palavra.upper()} tem as vogais: ', end=' ')
    
    for contagem in range(0, len(palavra)):
        if palavra[contagem] in ['a', 'e', 'i', 'o', 'u']:
            print(palavra[contagem], end='  ')
    
    print()
print()