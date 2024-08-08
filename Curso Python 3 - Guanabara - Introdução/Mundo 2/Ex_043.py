#Desenvolva uma lógica que leia o pesa e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
#-Abaixo de 18.5: Abaixo do Peso
#-Entre 18.5 e 25: Peso Ideal
#-25 até 30: Sobrepeso
#-30 até 40: Obesidade
#-Acima de 40: Obesidade Mórbida

print(f'\n{'- Me informe seu peso em (Kg) e sua altara em (m), e eu te informo seu IMC e o status do mesmo -':^101}\n')

pesoDoUsuário = float(input('Qual o seu peso(kg)? '))
alturaDoUsuário = float(input('Qaul a sua altura(m)? '))
imcDoUsuário = pesoDoUsuário / (alturaDoUsuário**2)

print(f'O seu IMC é de {imcDoUsuário:.1f}, você está', end=' ')

if imcDoUsuário < 18.5:
    print('Abaixo Do Peso.\n')

elif imcDoUsuário <= 25:
    print('no Peso Ideal.\n')

elif imcDoUsuário <= 30:
    print('com Sobrepeso.\n')

elif imcDoUsuário <= 40:
    print('com Obesidade.\n')

else:
    print('com Obesidade Mórbida.\n')