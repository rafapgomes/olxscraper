import getpage
import scrapepage
import arq
link = "https://www.olx.com.br/brasil?o=1&q=notebook%20ryzen%203"
page = getpage.request(link)

while(scrapepage.listpage(page)!=0):
    lista_anuncios = scrapepage.getadlist(page)
    anuncios_tratados = scrapepage.trataanucio(lista_anuncios)
    vet = []
    vet = scrapepage.getanunc(anuncios_tratados)
    arq.writearq(vet)
    link = scrapepage.listpage(page)
    print(link)
    page = getpage.request(link)
    print("-------------------------------------------------------------")




