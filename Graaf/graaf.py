import csv



# Makes a list with all the stations, x/y cordianates and if it is a critical station.
stations = []
with open ('stations.csv ') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        stations.append(row)
        

# Makes a list with all the connection and the time.
verbindingen = []
with open('verbindingen.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        verbindingen.append(row)

# Prints the station and the connection with the time.        
print(stations[0]['Station'])        
print(verbindingen[0]['Station1'], verbindingen[0]['Station2'], verbindingen[0]['Tijd'])
 
