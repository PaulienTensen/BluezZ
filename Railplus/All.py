# CHECKEN VOOOR FUNCTIE POP2()




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
        
        stat = []
        tijd = []
        
        if stations[i]['Station'] == verbindingen[z]['Station1']:
            
            stat.append(verbindingen[z]['Station2'])
            tijd.append(verbindingen[z]['Tijd'])
            u = stat, tijd            
            sporen.append(u)
          
        if stations[i]['Station'] == verbindingen[z]['Station2']:
            
            stat.append(verbindingen[z]['Station1'])
            tijd.append(verbindingen[z]['Tijd'])
            u = stat, tijd            
            sporen.append(u)
   
    alle_sporen.append(sporen)

    
    
graph = {}

# Makes the graph
for i in range (b):
    y = {}
    x= stations[i]['Station']
    g=alle_sporen[i]
    y = {x:g}
    graph.update(y)


    
    
    

    
    
    
# ZOEKEN NAAR DE UITHOEKEN VAN DE KAART    
uithoeken =[] 
geen_uithoek = 2   

for i in range (b):
    x = stations[i]['Station']
    connecties = len(graph[x])

    if connecties < geen_uithoek:
        uithoeken.append(x)
         


         
         
         
         
         
    
# Trein class aanmaken.    
class Trein(object):
    def __init__(self, traject, eindstation, beginstation, tijdsduur):
        self.traject= traject
        self.eindstation = eindstation
        self.tijdsduur = tijdsduur
        self.beginstation = beginstation
     
    # Vervangt oud station voor huidig station.
    def actuele_station(self,huidig_station):
        self.eindstation = []
        self.eindstation.append(huidig_station)
      
    # Volgend spoor bepalen. 
    def volgend_spoor(self, nieuw_station):
        self.traject.append(nieuw_station)
       
    # Tijd bijhouden.   
    def tijd(self, tijd):
        self.tijdsduur += tijd
        

    # De verbinding met de kortste tijd kiezen.
    # Hier worden alle beslissingen gemaakt kwa welk spoor te nemen
    # Hier moeten dus de restraints aangepast worden!
    def opties(self, huidig_station):
       

        richtingen = graph[huidig_station]

        stations_niet_aangetikt = []
        stations_wel_aangetikt = []
        terugweg = []

        
        # INDELEN
        for row in richtingen:

            #INDELING VAN SPOREN DIE GEREDEN ZIJN MOET NOG GEMAAKT WORDEN
            # MISSCHIEN EEN LIST MET DAARIN DE HUIDIGE SPOOR MET DE UITEINDELIJK 
            # BESTEMMING MAKEN ZODAT WE DAT MAKKELIJK KUNNE CHECKEN
            if row[0][0] not in trajecten_algemeen:
                stations_niet_aangetikt.append(row)
            elif row[0][0] == thomas.traject[-2]:
                terugweg.append(row) 
            else:
                stations_wel_aangetikt.append(row)
        
        
        #ISGOED!!:: NIET AANGETIKT :: KORSTE VERBINDING
        if not stations_niet_aangetikt == []:
            beste_tijd = 1000
            for row in stations_niet_aangetikt: 
                if int(row[1][0]) <= beste_tijd:
                    beste_tijd = int(row[1][0])
                    beste_station = row[0][0] 


           # IDEE OM BIJ TE HOUDEN OF WE ALLE STATIONS HEBBEN GEHAD??
           #if row[0][0] not in self.traject:
                #print row[0][0]
            trajecten_algemeen.append(beste_station)
            return beste_station, beste_tijd

        # ALS ALLE STATIONS ZIJN BEREDEN, KIES NIET DE TERUGWEG.
        # WEL KORTSTE ROUTE VAN DE BEREDEN SPOREN
        
       
        elif not stations_wel_aangetikt == []: 
            for row in stations_wel_aangetikt:
                beste_tijd = 1000
                if int(row[1][0]) <= beste_tijd:
                    beste_tijd = int(row[1][0])
                    beste_station = row [0][0]
            return beste_station, beste_tijd
            
        # ALS TERUG ENIGE OPTIE IS GA TERUG
        else: 
            beste_station = row[0][0]
            beste_tijd =  int(row[1][0])
            return beste_station, beste_tijd
 

 
    def pop(self):
        pop = self.traject.pop() 
        
    def pop2(self):
        pop = trajecten_algemeen.pop()
        
    def verminderen(self, laatste_verbinding):
        self.tijdsduur -= laatste_verbinding[1] 
        

        














# AUTOMATISEREN: AKA NIET ZELF NAMEN ERIN MOETEN TE DOEN!!::  
# MISSCHIEN OP DEZE MANIER, MAAR BETER KIJKEN NAAR DE LISTS:::::::

trajecten_algemeen =['Amsterdam Centraal']  

START = ['Amsterdam Centraal']       
thomas = Trein(START, START, ['Amsterdam Centraal'], 0)    

#print "TRAJECTEN ALGEMEEN1:: ", trajecten_algemeen 

# While loop gaat door tot traject is kleiner of gelijk dan 120.
while (thomas.tijdsduur < 120):


    # Beste optie kiezen aan de hand van de mogelijkheden.
    beste_optie = thomas.opties(thomas.eindstation[0])
    # Trein verplaatsen naar volgend spoor.
    thomas.volgend_spoor(beste_optie[0])
    # Huiding station updaten.
    thomas.actuele_station(beste_optie[0])
    # Tijd updaten.
    thomas.tijd(beste_optie[1])

# NIET VERWIJDEREN, BELANGRIJK VOOR ALS DE TRAJECTMAKER GOED WERKT   
#Al is het traject hoger betekent dat er 1 loop te veel gedaan is, dus die moet eraf gehaald worden.

if thomas.tijdsduur > 120:
    thomas.verminderen(beste_optie)
    thomas.pop()
    thomas.pop2()
    lengte = len(thomas.traject) - 1
    thomas.actuele_station(thomas.traject[lengte])
 
# ALGEMENE POP NOG TE DOEN !!!!!! VOOR ALLE TRAJECTEN, ZIE THOMAS _ HAARLEM 
#print "TRAJECTEN ALGEMEEN2:: ", trajecten_algemeen 
 
 

for i in range (b):
    x = stations[i]['Station']
    if not x in trajecten_algemeen:
        START = [x]
        



bram = Trein(START, START, ['Schiphol Airport'],0) 
 
 
 
 
 
# While loop gaat door tot traject is kleiner of gelijk dan 120.
while (bram.tijdsduur < 120):


    # Beste optie kiezen aan de hand van de mogelijkheden.
    beste_optie = bram.opties(bram.eindstation[0])
    # Trein verplaatsen naar volgend spoor.
    bram.volgend_spoor(beste_optie[0])
    # Huiding station updaten.
    bram.actuele_station(beste_optie[0])
    # Tijd updaten.
    bram.tijd(beste_optie[1])

# NIET VERWIJDEREN, BELANGRIJK VOOR ALS DE TRAJECTMAKER GOED WERKT   
#Al is het traject hoger betekent dat er 1 loop te veel gedaan is, dus die moet eraf gehaald worden.

if bram.tijdsduur > 120:
    bram.verminderen(beste_optie)
    bram.pop()
    bram.pop2()
    lengte = len(bram.traject) - 1
    bram.actuele_station(bram.traject[lengte])  

    
    
   


#print "TRAJECTEN ALGEMEEN voor NU:: ", trajecten_algemeen    

for i in range (b):
    x = stations[i]['Station']
    if not x in trajecten_algemeen:
        START = [x]
        


pau = Trein(START, START, ['Heemstede-Aerdenhout'],0)





while (pau.tijdsduur < 120):

    
    # Beste optie kiezen aan de hand van de mogelijkheden.
    beste_optie = pau.opties(pau.eindstation[0])
    # Trein verplaatsen naar volgend spoor.
    
    pau.volgend_spoor(beste_optie[0])
    # Huiding station updaten.
    pau.actuele_station(beste_optie[0])
    # Tijd updaten.
    pau.tijd(beste_optie[1])

# NIET VERWIJDEREN, BELANGRIJK VOOR ALS DE TRAJECTMAKER GOED WERKT   
#Al is het traject hoger betekent dat er 1 loop te veel gedaan is, dus die moet eraf gehaald worden.

if pau.tijdsduur > 120:
    pau.verminderen(beste_optie)
    pau.pop()
    pau.pop2()
    lengte = len(pau.traject) - 1
    pau.actuele_station(pau.traject[lengte])   

    
for i in range (b):
    x = stations[i]['Station']
    if not x in trajecten_algemeen:
        START = [x] 
        
        
mat = Trein(START, START, ['Den Helder'],0)





while (mat.tijdsduur < 120):

    
    # Beste optie kiezen aan de hand van de mogelijkheden.
    beste_optie = mat.opties(mat.eindstation[0])
    # Trein verplaatsen naar volgend spoor.
    
    mat.volgend_spoor(beste_optie[0])
    # Huiding station updaten.
    mat.actuele_station(beste_optie[0])
    # Tijd updaten.
    mat.tijd(beste_optie[1])

# NIET VERWIJDEREN, BELANGRIJK VOOR ALS DE TRAJECTMAKER GOED WERKT   
#Al is het traject hoger betekent dat er 1 loop te veel gedaan is, dus die moet eraf gehaald worden.

if mat.tijdsduur > 120:
    mat.verminderen(beste_optie)
    mat.pop()
    mat.pop2()
    lengte = len(mat.traject) - 1
    mat.actuele_station(mat.traject[lengte])           


for i in range (b):
    x = stations[i]['Station']
    if not x in trajecten_algemeen:
        START = [x] 

        
        
        
        
ben = Trein(START, START, ['Den Helder'],0)

while (ben.tijdsduur < 120):

    # Beste optie kiezen aan de hand van de mogelijkheden.
    beste_optie = ben.opties(ben.eindstation[0])
    # Trein verplaatsen naar volgend spoor.
    
    ben.volgend_spoor(beste_optie[0])
    # Huiding station updaten.
    ben.actuele_station(beste_optie[0])
    # Tijd updaten.
    ben.tijd(beste_optie[1])

# NIET VERWIJDEREN, BELANGRIJK VOOR ALS DE TRAJECTMAKER GOED WERKT   
#Al is het traject hoger betekent dat er 1 loop te veel gedaan is, dus die moet eraf gehaald worden.

if ben.tijdsduur > 120:
    ben.verminderen(beste_optie)
    ben.pop()
    ben.pop2()
    lengte = len(ben.traject) - 1
    ben.actuele_station(ben.traject[lengte])   

for i in range (b):
    x = stations[i]['Station']
    if not x in trajecten_algemeen:
        START = [x] 


print "TRAJECTEN ALGEMEEN:: ", trajecten_algemeen    
print
print
print
print "TRAJECT THOMAS::", thomas.traject
print
print "TRAJECT BRAM::", bram.traject
print
print "TRAJECT PAU::", pau.traject
print
print "TRAJECT MAT::", mat.traject
print
print "TRAJECT BEN::", ben.traject
    
    
