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
    
print graph['Haarlem'][1][0]



def make_traject(graph, start, end, path =[]):
    path = path + graph[start]
    if start == end:
        return [path]
    if not graph.has_key(start):
        return None
    
    
    
    print ("Start:")
    print path
    print("End:")
    print end

x = make_traject(graph, 'Beverwijk', 'Amsterdam Amstel')	

#def find_shortest_path(graph, start, end, path=[]):
   #     path = path + [start]
      #  if start == end:
     #   return path
     #   if not graph.has_key(start):
        #    return None
        #shortest = None
        #for node in graph[start]:
           # if node not in path:
              #  newpath = find_shortest_path(graph, node, end, path)
                #if newpath:
                   # if not shortest or len(newpath) < len(shortest):
                      #  shortest = newpath
        #return shortest	
		
    
    
