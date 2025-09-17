#Crie um código em Python que teste se o site Pudim.com.br está acessível pelo computador usado.

from webbrowser import open
from urllib import request,error

def verificandoSite():
    url = 'https://www.pudim.com.br'
    
    open(url)

    try:
        request.urlopen(url)

    except error.URLError:
        print('\nNão foi possivel abrir a url, site fora do ar!\n')

    else:
        print('\nFoi possivel abrir a url, site no ar!\n')

   
verificandoSite()