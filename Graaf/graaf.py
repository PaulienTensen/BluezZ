import csv

alle_sporen = []

# Makes a list with all the stations, x/y cordianates and if it is a critical station.
stations = []
with open ('stations.csv ') as csvfile:
    reader = csv.DictReader(csvfile)
    b = 0
    for row in reader:
        b = b+1
        stations.append(row)
        

# Makes a list with all the connection and the time.
verbindingen = []
with open('verbindingen.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    a = 0
    for row in reader:
        a = a+1
        verbindingen.append(row)


# Prints the station and the connection with the time. 


for i in range (b):  
   
    sporen = [] 
    for z in range (a):

        if stations[i]['Station'] == verbindingen[z]['Station1']:
    
            #print stations[i]['Station'], verbindingen[z]['Station2']
            
            sporen.append(verbindingen[z]['Station2'])
            #print sporen
            
    alle_sporen.append(sporen)




dict = {}

for i in range (b):
    b = {}
    x= stations[i]['Station']
    g=alle_sporen[i]
    b = {x:g}
    dict.update(b)

print dict


    
 
 
 
 
 


 

    