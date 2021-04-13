from bs4 import BeautifulSoup
import getpage

local = 'sc-7l84qu-1 ciykCV sc-ifAKCX dpURtf'
preco = 'sc-ifAKCX eoKYee'
imagem = 'sc-1q8ortj-0 gIkEbD'
lixo = 'fnmrjs-3 eJTbMD'
lixo2 = 'h3us20-3 csYflq'

proxpage = 'sc-1bofr6e-0 iRQkdN'

page = getpage.request()

def getadlist(page):
     soup = BeautifulSoup(page.content, 'html.parser')
     adlist = soup.find('ul',id="ad-list")
     lista_anuncios  = adlist.find_all('a')
     
     return lista_anuncios

lista_anuncios = getadlist(page)

def trataanucio(lista_anuncios):
    anuncios_tratados = []
    for anuncio in lista_anuncios:
        remove = anuncio.find(class_= imagem)
        remove.decompose()
        remove = anuncio.find(class_= lixo)
        remove.decompose()
        remove = anuncio.find(class_= lixo2)
        remove.decompose()
        anuncios_tratados.append(anuncio)
        
    return anuncios_tratados

def getlink(anuncios_tratados):
    for anuncio in anuncios_tratados:
        titulo = gettitulo(anuncio)
        if comptitulo(titulo) == 0:
            preco = convertepreco(getpreco(anuncio))
            if preco<3.5:
                print(anuncio.get('href'))
                print(formata(preco))
                

def comptitulo(titulo):
    for nome in titulo:
        if nome == 'NOTEBOOK':
           return 0

def gettitulo(anuncio):
    titulo = anuncio.find('h2').contents[0]
    titulo = titulo.upper().split()
    return titulo

def getpreco(anuncio):
    valor = anuncio.find(class_= preco)
    if len(valor.contents) != 0:
        return valor.contents[0].split()[1]
    

def convertepreco(preco):
    return float(preco)

def formata(preco):
    return format(preco, '.3f')

getlink(trataanucio(lista_anuncios))



