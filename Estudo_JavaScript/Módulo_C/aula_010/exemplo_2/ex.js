function somar(){
    var resultado = document.getElementById('resultadoSoma')

    var number1 = document.getElementById('number1')
    number1 = Number(number1.value)

    var number2 = document.getElementById('number2')
    number2 = Number(number2.value)

    resultado.innerHTML = `A soma entre ${number1} e ${number2} é igual à <strong>${number1 + number2}</strong>.`
}