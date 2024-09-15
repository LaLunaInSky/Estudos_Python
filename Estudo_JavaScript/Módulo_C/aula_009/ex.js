/* 
Entendo o DOM
 - O que é DOM? -
    Document Object Model

    Árvore DOM
    - window (parent de location, document, history)
        - location (child de window)
        
        - document (child de window) (parent de HTML)
            - HTML (child de document) (parent de head e body)
             - head (child de HTML) (parent das tags em <head>)
                -todas as tags criadas na tag <head> no documento html (child de head)

             - body (child de HTML) (parent das tags em <body>)
                -todas as tags criadas na tag <body> no documento html (child de head)

        - history (child de window)

 - Selecionando Elementos por DOM:
    por Marca:
        getElementsByTagName()
    por ID:
        getElementById()
    por Nome:
        getElementsByName()
    por Classe:
        getElementsByClassName()
    por Seletor
        querySelector()
        querySelectorAll()
*/

//Usando a child
/*
var corpo = document.body
*/

//Usando a Marca
/*
var p1 = document.getElementsByTagName('p')[1]
*/

//Usando o id
/*
var mensagem = document.getElementById('msg')
mensagem.style.color = "red"
mensagem.style.fontSize = "30px"
mensagem.innerText = 'Foi longe!'
mensagem.innerHTML = `<strong>${mensagem.innerText}<strong>`
*/

//Usando o name
/*
var mensagem = document.getElementsByName('msg')[0]
mensagem.innerText = 'Foi foi longe!'
*/

//Usando o Seletor
var mensagem = document.querySelector('div.msg')    //id = '#', class = '.'
mensagem.style.color = "red"
mensagem.style.fontSize = "30px"
mensagem.innerText = 'Foi longe!'
mensagem.innerHTML = `<strong>${mensagem.innerText}<strong>`