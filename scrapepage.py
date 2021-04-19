from bs4 import BeautifulSoup
import getpage

local = 'sc-7l84qu-1 ciykCV sc-ifAKCX dpURtf'
preco = 'sc-ifAKCX eoKYee'
imagem = 'sc-1q8ortj-0 gIkEbD'
lixo = 'fnmrjs-3 eJTbMD'
lixo2 = 'h3us20-3 csYflq'

proxpage= 'sc-hmzhuo kJjuHR sc-jTzLTM iwtnNi'

#sc-1bofr6e-1 iUNkan sc-ifAKCX bBbnjQ

paginas = "sc-hmzhuo fFyjgz sc-jTzLTM iwtnNi"


def getadlist(page):
     soup = BeautifulSoup(page.content, 'html.parser')
     adlist = soup.find('ul',id="ad-list")
     lista_anuncios  = adlist.find_all('a')
     
     return lista_anuncios


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


def comptitulo(titulo,namecomp):
    titulo = split(titulo)
    for nome in titulo:
        if nome == namecomp:
           return 0

def gettitulo(anuncio):
    titulo = anuncio.find('h2').contents[0]
    titulo = titulo.upper()
    return titulo

def split(string):
   return string.split()

def getpreco(anuncio):
    valor = anuncio.find(class_= preco)
    if len(valor.contents) != 0:
        string = split(valor.contents[0])
        return string[1]
    else:
        return 0
    

def convertepreco(preco):
    return float(preco)

def formata(preco):
    return format(preco, '.3f')

def add_lista(lista_anuncios,anuncio,preco):
    
    lista_anuncios.append(gettitulo(anuncio))
    lista_anuncios.append(formata(preco))
    lista_anuncios.append(getlocal(anuncio))
    lista_anuncios.append((anuncio.get('href')))

def imprimelista(lista):
    for item in lista:
        print(item)

def getlocal(anuncio):
    localizacao = anuncio.find(class_  = local)
    return localizacao.contents[0]

def getanunc(anuncios_tratados,compname):
    lista_anuncios = []
    for anuncio in anuncios_tratados:
        titulo = gettitulo(anuncio)
        titulo = comptitulo(titulo,compname)
        local = getlocal(anuncio)
        if titulo == 0:
            preco = getpreco(anuncio)
            preco = convertepreco(preco)
            if preco<3.5:
               lista_temp = []

               add_lista(lista_temp,anuncio,preco)    
               lista_anuncios.append(lista_temp)
    
    return lista_anuncios


def listpage(page):
    lista_page = []
    soup = BeautifulSoup(page.content, 'html.parser')
    link = soup.find_all(class_= "sc-1bofr6e-0 iRQkdN")
    for item in link:
         i = item.find(class_= "sc-1bofr6e-1 iUNkan sc-ifAKCX bBbnjQ")
         i = i.contents[0].upper().split()
         if comppage(i)==1:
             return (item.get('href'))
         
    return 0
    

    


def comppage(nome):
        for string in nome:
            if string == 'PRÓXIMA':
                return 1



