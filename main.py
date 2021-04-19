import getpage
import scrapepage
import arq

item = "notebook ryzen 3"
link = getpage.getlink(item)

page = getpage.request(link)

while(scrapepage.listpage(page)!=0):

    lista_anuncios = scrapepage.getadlist(page)
    anuncios_tratados = scrapepage.trataanucio(lista_anuncios)
    vet = []
    vet = scrapepage.getanunc(anuncios_tratados,"NOTEBOOK")
    arq.writearq(vet)
    link = scrapepage.listpage(page)
    print(link)

    page = getpage.request(link)
    print("-------------------------------------------------------------")




