# Rail NL 

De case Rail NL gaat over het maken van de lijnvoering van intercity treinen in Nederland. De case is opgesplitst in twee delen. Allereerst wordt gekeken naar de lijnvoering voor Holland, om dit vervolgens uit te breiden naar de lijnvoering voor heel Nederland. 
Binnen een gegeven tijdsframe van 2 uur worden een aantal trajecten uitgezet. Onder trajecten wordt een route van sporen en stations waarover treinen heen en weer rijden, verstaan.

Aantal treinstations in Holland: 22, 
aantal treinstations in Nederland: 118. 

Verder moet er in deze case rekening worden gehouden met 'kritieke stations', met bijbehorende 'kritieke sporen'. Wanneer deze stations niet regelmatig worden bereden, treden er logistieke problemen op. 

De volgende score functie werd meegegeven bij de case voor de kwaliteit van de lijnvoering: 
s = p*10000 - (t*20 + min/100000)
Waarin S de score is, p het percentage van de bereden kritieke verbindingen, t het aantal treinen en m het totaal door alle treinen samen gereden aantal minuten in de lijnvoering. 

### Voorwaarden

Zorg dat de bijbehorende csv bestanden: ConnectiesHolland.csv, StationsHolland.csv voor Holland in dezelfde map staan als het bijbehorende python bestand. 

### Instaleren

Deze case is gemaakt met behulp van Python 3.0

#### Runnen
python graaf.py

### Toetsingsgrootheid

De toetsingsgrootheid van deze case is (n-1)! / 2. Waarbij n het aantal stations zijn. 

### Algoritmes

In deze case is gebruik gemaakt van verschillende algoritmes. 




## Auteurs
Paulien Tensen, Matia Caso & Thomas van Dooren. 







