from bs4 import BeautifulSoup
import getpage

imagem = 'sc-1q8ortj-0 gIkEbD'
lixo = 'fnmrjs-3 eJTbMD'
lixo2 = 'h3us20-3 csYflq'
page = getpage.request()

def getadlist(page):
     soup = BeautifulSoup(page.content, 'html.parser')
     adlist = soup.find('ul',id="ad-list")
     lista_anuncios  = adlist.find_all('a')
     
     return lista_anuncios

lista_anuncios = getadlist(page)

def trataanucio(lista_anuncios):
    
    for anuncio in lista_anuncios:
        remove = anuncio.find(class_= imagem)
        remove.decompose()
        remove = anuncio.find(class_= lixo)
        remove.decompose()
        remove = anuncio.find(class_= lixo2)
        remove.decompose()
        print(anuncio.prettify())
        
        return 
    return anuncios_tratados
        
    

trataanucio(lista_anuncios)
