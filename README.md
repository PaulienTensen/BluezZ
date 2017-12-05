# Rail NL 

De case Rail NL gaat over het maken van de lijnvoering van intercity treinen in Nederland. De case is opgesplitst in twee delen. Allereerst wordt gekeken naar de lijnvoering voor Holland, om dit vervolgens uit te breiden naar de lijnvoering voor heel Nederland. 
Binnen een gegeven tijdsframe van 2 uur worden een aantal trajecten uitgezet. Onder trajecten wordt een route van sporen en stations waarover treinen heen en weer rijden, verstaan.

Aantal treinstations in Holland: 22, 
aantal treinstations in Nederland: 118. 

Verder moet er in deze case rekening worden gehouden met 'kritieke stations', met bijbehorende 'kritieke sporen'. Wanneer deze stations niet regelmatig worden bereden, treden er logistieke problemen op. 

De volgende score functie werd meegegeven bij de case voor de kwaliteit van de lijnvoering: 
s = p*10000 - (t*20 + min/100000)
Waarin S de score is, p het percentage van de bereden kritieke verbindingen, t het aantal treinen en m het totaal door alle treinen samen gereden aantal minuten in de lijnvoering. 

constrains deel 1 - Lijnvoering voor Holland:
1. Tijdsframe van trajecten: maximaal 2 uur. 
2. Alle stations moeten bereden worden binnen de 2 uur. 
3. Maximaal aantal trajecten: 7. 
(4. Alle sporen moeten bereden worden binnen 2 uur met het maximal aantal toegestane trajecten)

constrains deel 2 - Lijnvoering voor Nederland:
1. Tijdsframe van trajecten: maximaal 3 uur. 
2. Alle stations moeten bereden worden binnen 3 uur. 
3. Maximaal aantal trajecten: 20. 
(4. Alle sporen moeten bereden worden binnen 3 uur met het maximaal aantal toegestane trajecten).

### Voorwaarden

Zorg dat de bijbehorende csv bestanden: ConnectiesHolland.csv, StationsHolland.csv voor Holland in dezelfde map staan als het bijbehorende python bestand. 

### Installeren

Deze case is gemaakt met behulp van Python 3.6

#### Runnen:
python graaf.py
python matrix.py

### Toetsingsgrootheid

De toetsingsgrootheid van deze case is het gemiddelde aantal sporen per station ^(aantal stations).


### Probleem type
constrained optimalization problem (COP). Hierbij moet een zo goed mogelijke oplossing worden gevonden. 
De bijbehorende toetsingsgrootheid is ************

Grootte statespace: 
upperbound: slechtste oplossing (nearest neighbour algoritme): uitrekenen wat de totale traject lengte is. 
aantal minuten / 120 

Lowerbound: de hoogste score die we kunnen krijgen.



### Algoritmes

In deze case wordt gebruik gemaakt van een ongerichte graaf. Aangezien je heen en weer kunt tussen knopen(stations).
Het tweede algoritme dat wordt toegepast is een 'hill climber'
Het derde algoritme dat wordt toegepast is 'stimulated annealing'. 



## Auteurs
Paulien Tensen, Matia Caso & Thomas van Dooren. 







