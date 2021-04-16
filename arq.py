import csv

f = open('notebooks.csv', 'w', newline='', encoding='utf-8')
w = csv.writer(f)


def writearq(lista):
  
            
    for vet in lista:
            w.writerow(vet)    
   
          