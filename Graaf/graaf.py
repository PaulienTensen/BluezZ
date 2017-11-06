import csv



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
    print(stations[i]['Station']) 

for i in range (a):      
    print(verbindingen[i]['Station1'], verbindingen[i]['Station2'], verbindingen[i]['Tijd'])
 
