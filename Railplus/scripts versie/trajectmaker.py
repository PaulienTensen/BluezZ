import start
import csv
import inladen
import algo1
import start

def traject_maker(RANGE, MAX, STATIONS, VERBINDINGEN):

    #Maken van de te gebruiken lists.
    stations = inladen.stations(STATIONS)
    verbindingen = inladen.verbindingen(VERBINDINGEN)

    alle_sporen = inladen.alle_sporen(stations, verbindingen)
    graph = inladen.graph(stations, alle_sporen)
    uithoeken = inladen.uithoeken(graph, stations)
    
    alle_trajecten = []
    trajecten_algemeen =[] 
    sporen = [] 
    alle_tijdsduur = []
    
    
    for i in range (RANGE):

        START = start.kies_start(sporen, verbindingen, uithoeken, trajecten_algemeen, stations)
        z = START
        
        trein = algo1.Trein([START], [START], [z], 0)    

        # While loop gaat door tot traject is kleiner of gelijk dan 120.
        while (trein.tijdsduur < MAX):

            # Beste optie kiezen aan de hand van de mogelijkheden.
            beste_optie = trein.opties(sporen, graph, trajecten_algemeen, trein.eindstation[0])
            #Spoor toevoegen.
            trein.spoor_toevoegen(sporen, trein.eindstation[0], beste_optie)
            # Trein verplaatsen naar volgend spoor.
            trein.volgend_spoor(beste_optie[0])
            # Huiding station updaten.
            trein.actuele_station(beste_optie[0])
            # Tijd updaten.
            trein.tijd(beste_optie[1])


        if trein.tijdsduur > MAX:
            trein.verminderen(beste_optie)
            trein.pop(trajecten_algemeen, sporen)
            lengte = len(trein.traject) - 1
            trein.actuele_station(trein.traject[lengte])
        
        
        alle_trajecten.append(trein.traject)
        alle_tijdsduur.append(trein.tijdsduur)

    return alle_tijdsduur, alle_trajecten, sporen

    