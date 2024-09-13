var num1 = Number(window.prompt("Digite um número"))
var num2 = Number(window.prompt("Digite outro número"))

//Number.parseInt(n) e Number.parseFloat(n) conversão para Inteiro e Real
//String(n) ou n.toString() conversão para String

var frase = `A soma dos números ${num1} e ${num2} é igual a ${num1 + num2}.` // uso de template string

/*
Formatando Strings:
- n.length  //quantos caracteres a string tem
- n.toUpperCase()   //transforma a string toda em MAIÚSCULA
- n.toLowerCase()   //transfroma a string toda em minúscula
*/

document.write(`
    <p>
        ${frase} <br>
        A frase tem ${frase.length} letras no total. <br>
        ${frase.toUpperCase()} <br>
        ${frase.toLowerCase()}
    </p>
`) //escreve no documento html o resultado da string, com uso de tags html

/*
Formatação Float:
- n.toFixed(x)  //x é a quantidade de unidades depois do ponto. Porém retorna uma string como parâmetro final
- n.replace('x', 'y')   //x é o o parâmetro da string que vai ser substituida por y, apenas para String.
- n.toLocaleString('pt-BR', {style: 'currency', currency: 'BRL'})   //resultado fica 'R$ 0,00', localiza o float para o modelo e moeda do pais escolhido como no exemplo acima
*/