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
        twee_stappen_terug = []
        terugweg = []
        
        
        
        
        
        # INDELEN
        for row in richtingen:

            
        
            if row[0][0] not in self.traject:
                stations_niet_aangetikt.append(row)
            elif row[0][0] == thomas.traject[-2]:
                terugweg.append(row)
            elif row[0][0] == thomas.traject[-3]:
                twee_stappen_terug.append(row)
            else:
                stations_wel_aangetikt.append(row)
        
        
        # WERKT NOG NIET, LEGE APPENDS, MAAR HOEZO???????
        print twee_stappen_terug
        
        
        
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
            return beste_station, beste_tijd

           
        # ALS ALLE SPOREN ZIJN BEREDEN, KIES NIET DE TERUGWEG.
        # WEL KORTSTE ROUTE VAN DE BEREDEN SPOREN
        
       
        elif not stations_wel_aangetikt == []: 

            for row in stations_wel_aangetikt:

                beste_tijd = 1000
                
                if int(row[1][0]) <= beste_tijd:
                    beste_tijd = int(row[1][0])
                    beste_station = row [0][0]
            
            # IDEE OM BIJ TE HOUDEN OF WE ALLE STATIONS HEBBEN GEHAD??
            #if row[0][0] not in self.traject:
              #  print row[0][0]
                
                
            return beste_station, beste_tijd
          
          
        elif not twee_stappen_terug == []:
            
            beste_station = row[0][0]
            beste_tijd =  int(row[1][0])
            
            return beste_station, beste_tijd
            
          
        # ALS TERUG ENIGE OPTIE IS GA TERUG
        else: 
            beste_station = row[0][0]
            beste_tijd =  int(row[1][0])
            return beste_station, beste_tijd
                    
                
                
                

    

    def pop(self):
        pop = self.traject.pop()
        
    
    def verminderen(self, laatste_verbinding):
        self.tijdsduur -= laatste_verbinding[1] 
        

        


# AUTOMATISEREN: AKA NIET ZELF NAMEN ERIN MOETEN TE DOEN!!::  
# MISSCHIEN OP DEZE MANIER, MAAR BETER KIJKEN NAAR DE LISTS:::::::


START = ['Amsterdam Centraal']   
      
# Trein initialiseren (beginpunt kiezen & tijd op nul zetten).        
thomas = Trein(START, START, ['Amsterdam Centraal'], 0)    



# While loop gaat door tot traject is kleiner of gelijk dan 120.
while (thomas.tijdsduur < 800):


    # Beste optie kiezen aan de hand van de mogelijkheden.
    beste_optie = thomas.opties(thomas.eindstation[0])
    # Trein verplaatsen naar volgend spoor.
    thomas.volgend_spoor(beste_optie[0])
    # Huiding station updaten.
    thomas.actuele_station(beste_optie[0])
    # Tijd updaten.
    thomas.tijd(beste_optie[1])
    
    #print thomas.traject
  













  
# NIET VERWIJDEREN, BELANGRIJK VOOR ALS DE TRAJECTMAKER GOED WERKT   
#Al is het traject hoger betekent dat er 1 loop te veel gedaan is, dus die moet eraf gehaald worden.

#if thomas.tijdsduur > 120:
  #  thomas.verminderen(beste_optie)
    #thomas.pop()
    #lengte = len(thomas.traject) - 1
    #thomas.actuele_station(thomas.traject[lengte])
 
 
 
 
   

print "HOLLAAAA AT ME"
print "THOMAS: :"
print
print "traject: ", thomas.traject
print "tijdsduur: ", thomas.tijdsduur
print "Beginstation: ", thomas.beginstation
print "Eindstation: ", thomas.eindstation

