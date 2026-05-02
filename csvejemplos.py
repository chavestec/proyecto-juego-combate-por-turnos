import csv

with open('Personajes.txt','r') as csv_file:
    csv_reader=csv.DictReader(csv_file)
    fieldnames=['Personajes','Vida','Ataque','Defensa']
    
    
        
        print (line['personaje'])
