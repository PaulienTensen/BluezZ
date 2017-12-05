# STAAT ALLEMAAL  NU OP NATIONAAL
import algo2
import trajectmaker
import minuten
import hillclimber
import inladen

# 2 nodige globals.
HILL = 10000
MAX = 180
RANGE = 10
STATIONS = 'StationsNationaal.csv'
VERBINDINGEN = 'ConnectiesNationaal.csv' 

#MAKEN VAN DE TE GEBRUIKEN LISTS
stations = inladen.stations(STATIONS)
verbindingen = inladen.verbindingen(VERBINDINGEN)
alle_sporen = inladen.alle_sporen(stations, verbindingen)
graph = inladen.graph(stations, alle_sporen)
uithoeken = inladen.uithoeken(graph, stations)

#MAKEN VAN DE EERSTE OPLOSSING EN DIE INDELEN
trajecten = trajectmaker.traject_maker(RANGE, MAX, stations, verbindingen, uithoeken, graph)
alle_tijdsduur_oud = trajecten[0]
alle_trajecten_oud = trajecten[1]
sporen_oud = trajecten[2]
trajecten_algemeen_oud = trajecten[3]

# SCORE UITREKENEN
totale_tijdsduur_oud = minuten.minuten(alle_tijdsduur_oud)
score_oud = algo2.score(alle_trajecten_oud, totale_tijdsduur_oud, sporen_oud)

#HILLCLIMBER TOEPASSEN
resultaat = hillclimber.hillclimber(score_oud, alle_trajecten_oud, alle_tijdsduur_oud, HILL, RANGE, MAX, stations, verbindingen, uithoeken, graph, trajecten_algemeen_oud, sporen_oud)

score = resultaat[0]
alle_tijdsduur = resultaat[1]
alle_trajecten = resultaat[2]
sporen = resultaat[3]
trajecten_algemeen = resultaat[4]

print("TRAJECTEN::")
for i in range (len(alle_trajecten)):
    print()
    print("TRAJECT", i)
    print(alle_trajecten[i])
    print(alle_tijdsduur[i])
    
print()
print("SCORE WAS::", score_oud)
print("AANTAL SPOREN WAS::", len(sporen_oud))
print("AANTAL STATIONS WAS::", len(trajecten_algemeen_oud))
print()

print()
print("SCORE :::", score)
print("AANTAL SPOREN:: ", len(sporen))
print("AANTAL STATIONS:: ", len(trajecten_algemeen))







