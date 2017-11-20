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
    b = {}
    x= stations[i]['Station']
    g=alle_sporen[i]
    b = {x:g}
    graph.update(b)
    

    
    
    
    
    
    
    
    
      
    
    
    
    
    
    
    
    
    
    
    
    
    
# Trein class aanmaken.    
class Trein(object):
    def __init__(self, traject, beginstation, tijdsduur):
        self.traject= traject
        self.beginstation = beginstation
        self.tijdsduur = tijdsduur
     
    # Vervangt oud station voor huidig station.
    def actuele_station(self,huidig_station):
        self.beginstation = []
        self.beginstation.append(huidig_station)
      
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
        best_time = int(richtingen[0][1][0])
        best_station = richtingen[0][0][0]
        
        for row in richtingen:
            
            tijd = int(row[1][0])
            if tijd <= best_time:
                best_time = tijd
                best_station = row[0][0]

        return best_station, best_time
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    def pop(self):
        pop = self.traject.pop()
        
    
    def verminderen(self, laatste_verbinding):
        thomas.tijdsduur -= laatste_verbinding[1] 
        

START = ["Den Helder"]    
        
# Trein initialiseren (beginpunt kiezen & tijd op nul zetten).        
trajectthomas = START   
thomas = Trein(trajectthomas, START, 0)    






# While loop gaat door tot traject is kleiner of gelijk dan 120.
while (thomas.tijdsduur <= 120):

    # Beste optie kiezen aan de hand van de mogelijkheden.
    beste_optie = thomas.opties(thomas.beginstation[0])

    # Trein verplaatsen naar volgend spoor.
    thomas.volgend_spoor(beste_optie[0])

    # Huiding station updaten.
    thomas.actuele_station(beste_optie[0])

    # Tijd updaten.
    thomas.tijd(beste_optie[1])

#Al is het traject hoger betekent dat er 1 loop te veel gedaan is, dus die moet eraf gehaald worden.
if thomas.tijdsduur > 120:
    thomas.verminderen(beste_optie)
    thomas.pop()
    lengte = len(thomas.traject) - 1
    thomas.actuele_station(thomas.traject[lengte])
    
    
    




print
print


print
print "DEEL 2 :"
print


print "traject: ", thomas.traject
print "tijdsduur: ", thomas.tijdsduur
print "beginstation: ", thomas.beginstation




        
        
        
        
        
        
    #def nieuw_station(self, nieuw_station):
      #  self.stations.append(nieuw_station)
        
        
        
        
        

  


  
#mensenlijst = ['jan', 'harry']






#volgend_station = []




#nog_meer_mensen = ['mattia', 'paulien']


#thomas.instappen(nog_meer_mensen)



#thomas.waar_kan_ik_heen('Haarlem')

#thomas.nieuw_station('Haarlem')


#print(thomas.mensen)
#print len(thomas.mensen)
#print(thomas.stations)

