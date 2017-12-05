# STAAT ALLEMAAL  NU OP NATIONAAL
import algo2
import trajectmaker
import minuten

# 2 nodige globals.
MAX = 120
RANGE = 3
STATIONS = 'stations.csv'
VERBINDINGEN = 'verbindingen.csv' 

trajecten = trajectmaker.traject_maker(RANGE, MAX, STATIONS, VERBINDINGEN)

alle_tijdsduur = trajecten[0]
alle_trajecten = trajecten[1]
sporen = trajecten[2]


totale_tijdsduur = minuten.minuten(alle_tijdsduur)
score = algo2.score(alle_trajecten, totale_tijdsduur, sporen)


print(score)










