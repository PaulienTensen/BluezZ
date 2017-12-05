# STAAT ALLEMAAL  NU OP NATIONAAL

import csv
import inladen
import algo1
import start

# 2 nodige globals.
trajecten_algemeen =[] 
sporen = [] 
MAX = 180

#Maken van de te gebruiken lists.
stations = inladen.stations('StationsNationaal.csv')
verbindingen = inladen.verbindingen('ConnectiesNationaal.csv')

alle_sporen = inladen.alle_sporen(stations, verbindingen)
graph = inladen.graph(stations, alle_sporen)
uithoeken = inladen.uithoeken(graph, stations)






#TREIN 1
START = start.kies_start(sporen, verbindingen, uithoeken, trajecten_algemeen, stations)
z = START

thomas = algo1.Trein([START], [START], [z], 0)    

# While loop gaat door tot traject is kleiner of gelijk dan 120.
while (thomas.tijdsduur < MAX):

    # Beste optie kiezen aan de hand van de mogelijkheden.
    beste_optie = thomas.opties(sporen, graph, trajecten_algemeen, thomas.eindstation[0])
    #Spoor toevoegen.
    thomas.spoor_toevoegen(sporen, thomas.eindstation[0], beste_optie)
    # Trein verplaatsen naar volgend spoor.
    thomas.volgend_spoor(beste_optie[0])
    # Huiding station updaten.
    thomas.actuele_station(beste_optie[0])
    # Tijd updaten.
    thomas.tijd(beste_optie[1])


if thomas.tijdsduur > MAX:
    thomas.verminderen(beste_optie)
    thomas.pop(trajecten_algemeen, sporen)
    lengte = len(thomas.traject) - 1
    thomas.actuele_station(thomas.traject[lengte])
    
    
    
    

    
# TREIN 2
START = start.kies_start(sporen, verbindingen, uithoeken, trajecten_algemeen, stations)
z = START

bram = algo1.Trein([START], [START], [z],0) 


# While loop gaat door tot traject is kleiner of gelijk dan 120.
while (bram.tijdsduur < MAX):

    # Beste optie kiezen aan de hand van de mogelijkheden.
    beste_optie = bram.opties(sporen, graph, trajecten_algemeen, bram.eindstation[0])
    #Spoor toevoegen.
    verbinding = bram.spoor_toevoegen(sporen, bram.eindstation[0], beste_optie)
    # Trein verplaatsen naar volgend spoor.
    bram.volgend_spoor(beste_optie[0])
    # Huiding station updaten.
    bram.actuele_station(beste_optie[0])
    # Tijd updaten.
    bram.tijd(beste_optie[1])


if bram.tijdsduur > MAX:
    bram.verminderen(beste_optie)
    bram.pop(trajecten_algemeen, sporen)
    lengte = len(bram.traject) - 1
    bram.actuele_station(bram.traject[lengte])


    
     
#TREIN 3   
START = start.kies_start(sporen, verbindingen, uithoeken, trajecten_algemeen, stations)
z = START

pau = algo1.Trein([START], [START], [z],0)


while (pau.tijdsduur < MAX):


    # Beste optie kiezen aan de hand van de mogelijkheden.
    beste_optie = pau.opties(sporen, graph, trajecten_algemeen, pau.eindstation[0])
    #Spoor toevoegen.
    pau.spoor_toevoegen(sporen, pau.eindstation[0], beste_optie)
    # Trein verplaatsen naar volgend spoor.
    pau.volgend_spoor(beste_optie[0])
    # Huiding station updaten.
    pau.actuele_station(beste_optie[0])
    # Tijd updaten.
    pau.tijd(beste_optie[1])


if pau.tijdsduur > MAX:
    
    pau.verminderen(beste_optie)
    pau.pop(trajecten_algemeen, sporen)
    lengte = len(pau.traject) - 1
    pau.actuele_station(pau.traject[lengte])
    
    
    
    
    
    
#TREIN 4
START = start.kies_start(sporen, verbindingen, uithoeken, trajecten_algemeen, stations)
z = START


mat = algo1.Trein([START], [START], [z], 0)

while (mat.tijdsduur < MAX):

    # Beste optie kiezen aan de hand van de mogelijkheden.
    beste_optie = mat.opties(sporen, graph, trajecten_algemeen, mat.eindstation[0])
    #Spoor toevoegen.
    mat.spoor_toevoegen(sporen, mat.eindstation[0], beste_optie)
    # Trein verplaatsen naar volgend spoor.
    mat.volgend_spoor(beste_optie[0])
    # Huiding station updaten.
    mat.actuele_station(beste_optie[0])
    # Tijd updaten.
    mat.tijd(beste_optie[1])

    
if mat.tijdsduur > MAX:
    mat.verminderen(beste_optie)
    mat.pop(trajecten_algemeen, sporen)
    lengte = len(mat.traject) - 1
    mat.actuele_station(mat.traject[lengte])         


    
    
    
    
#TREIN 5
START = start.kies_start(sporen, verbindingen, uithoeken, trajecten_algemeen, stations)
z = START

ben = algo1.Trein([START], [START], [z], 0)

while (ben.tijdsduur < MAX):

    # Beste optie kiezen aan de hand van de mogelijkheden.
    beste_optie = ben.opties(sporen, graph, trajecten_algemeen, ben.eindstation[0])
    #Spoor toevoegen.
    ben.spoor_toevoegen(sporen, ben.eindstation[0], beste_optie)
    # Trein verplaatsen naar volgend spoor.
    ben.volgend_spoor(beste_optie[0])
    # Huiding station updaten.
    ben.actuele_station(beste_optie[0])
    # Tijd updaten.
    ben.tijd(beste_optie[1])

    
if ben.tijdsduur > MAX:
    ben.verminderen(beste_optie)
    ben.pop(trajecten_algemeen, sporen)
    lengte = len(ben.traject) - 1
    ben.actuele_station(ben.traject[lengte])
    
   





 #TREIN 6  
START = start.kies_start(sporen, verbindingen, uithoeken, trajecten_algemeen, stations)
z = START

ravi = algo1.Trein([START], [START], [z], 0)

while (ravi.tijdsduur < MAX):

    # Beste optie kiezen aan de hand van de mogelijkheden.
    beste_optie = ravi.opties(sporen, graph, trajecten_algemeen, ravi.eindstation[0])
    #Spoor toevoegen.
    ravi.spoor_toevoegen(sporen, ravi.eindstation[0], beste_optie)
    # Trein verplaatsen naar volgend spoor.
    ravi.volgend_spoor(beste_optie[0])
    # Huiding station updaten.
    ravi.actuele_station(beste_optie[0])
    # Tijd updaten.
    ravi.tijd(beste_optie[1])

    
if ravi.tijdsduur > MAX:
    ravi.verminderen(beste_optie)
    ravi.pop(trajecten_algemeen, sporen)
    lengte = len(ravi.traject) - 1
    ravi.actuele_station(ravi.traject[lengte])
    
    
    
    
#TREIN 7  
START = start.kies_start(sporen, verbindingen, uithoeken, trajecten_algemeen, stations)
z = START

daan = algo1.Trein([START], [START], [z], 0)

while (daan.tijdsduur < MAX):

    # Beste optie kiezen aan de hand van de mogelijkheden.
    beste_optie = daan.opties(sporen, graph, trajecten_algemeen, daan.eindstation[0])
    #Spoor toevoegen.
    daan.spoor_toevoegen(sporen, daan.eindstation[0], beste_optie)
    # Trein verplaatsen naar volgend spoor.
    daan.volgend_spoor(beste_optie[0])
    # Huiding station updaten.
    daan.actuele_station(beste_optie[0])
    # Tijd updaten.
    daan.tijd(beste_optie[1])

    
if daan.tijdsduur > MAX:
    daan.verminderen(beste_optie)
    daan.pop(trajecten_algemeen, sporen)
    lengte = len(daan.traject) - 1
    daan.actuele_station(daan.traject[lengte])
 


#TREIN 8  
START = start.kies_start(sporen, verbindingen, uithoeken, trajecten_algemeen, stations)
z = START

stijn = algo1.Trein([START], [START], [z], 0)
 
while (stijn.tijdsduur < MAX):

    # Beste optie kiezen aan de hand van de mogelijkheden.
    beste_optie = stijn.opties(sporen, graph, trajecten_algemeen, stijn.eindstation[0])
    #Spoor toevoegen.
    stijn.spoor_toevoegen(sporen, stijn.eindstation[0], beste_optie)
    # Trein verplaatsen naar volgend spoor.
    stijn.volgend_spoor(beste_optie[0])
    # Huiding station updaten.
    stijn.actuele_station(beste_optie[0])
    # Tijd updaten.
    stijn.tijd(beste_optie[1])

    
if stijn.tijdsduur > MAX:
    stijn.verminderen(beste_optie)
    stijn.pop(trajecten_algemeen, sporen)
    lengte = len(stijn.traject) - 1
    stijn.actuele_station(stijn.traject[lengte])
    
    
    
    
    
    
    
    
print() 
print('THOMAS:: ',thomas.traject)
print(thomas.tijdsduur)
print( 'BRAM:: ',bram.traject)
print(bram.tijdsduur)
print( 'PAU:: ',pau.traject) 
print( pau.tijdsduur)
print( 'MAT:: ',mat.traject)
print( mat.tijdsduur)
print( 'BEN:: ',ben.traject)
print( ben.tijdsduur)
print("RAVI:: ", ravi.traject)
print(ravi.tijdsduur)
print("DAAN:: ", daan.traject)
print(daan.tijdsduur)
print("STIJN:: ", stijn.traject)
print(stijn.tijdsduur)
print()
print( 'ALLE STATIONS:: ', len(trajecten_algemeen))
print()
print( 'ALLE VERBINDINGEN:: ', len(sporen))

