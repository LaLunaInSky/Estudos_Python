#Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

print(f'\n{'- Informe um número, e te mostrarei a sua tabuada -':^56}\n')

númeroInformado = int(input('Qual o número? '))

print(f'''\n{'=':=^15}
{f'{númeroInformado} X  1 = {númeroInformado*1}':^15}
{f'{númeroInformado} X  2 = {númeroInformado*2}':^15}
{f'{númeroInformado} X  3 = {númeroInformado*3}':^15}
{f'{númeroInformado} X  4 = {númeroInformado*4}':^15}
{f'{númeroInformado} X  5 = {númeroInformado*5}':^15}
{f'{númeroInformado} X  6 = {númeroInformado*6}':^15}
{f'{númeroInformado} X  7 = {númeroInformado*7}':^15}
{f'{númeroInformado} X  8 = {númeroInformado*8}':^15}
{f'{númeroInformado} X  9 = {númeroInformado*9}':^15}
{f'{númeroInformado} X 10 = {númeroInformado*10}':^15}
{'=':=^15}
\n''')