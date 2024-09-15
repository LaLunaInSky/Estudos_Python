//Continuação de DOM
/*
Eventos DOM
 - mouseenter
 - mousemove
 - mousedown
 - mouseup
 - click
 - mouseout
*/
var area = document.getElementById('area')
area.addEventListener(
    'click', clicar
)
area.addEventListener(
    'mouseenter', entrada
)
area.addEventListener(
    'mouseout', saida
)

function clicar(){
    area.innerText = 'Clicado!'
    area.style.background = 'red'
}

function entrada(){
    area.innerText = 'Entrou!'
}

function saida(){
    area.innerText = 'Saiu!'
    area.style.background = 'darkcyan'
}