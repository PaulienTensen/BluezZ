def kies_start(sporen, verbindingen, uithoeken, trajecten_algemeen, stations):
    b = len(stations)
    
    # Uithoeken eerst.
    for plek in uithoeken:
        if not plek in trajecten_algemeen:
            z = plek
            trajecten_algemeen.append(z)
            return z

    # Stations die niet zijn aangeraakt komen hierna.
    for i in range (b):
        plek = stations[i]['Station']
        if not plek in trajecten_algemeen:
            z = plek
            trajecten_algemeen.append(z)
            return z

    
    # Niet gereden verbindingen komen als laatst
    for i in range (len(verbindingen)):
        station1 = verbindingen[i]['Station1']
        station2 = verbindingen[i]['Station2']
        verbinding1 = {station1:station2}
        verbinding2 = {station2:station1}
        if not verbinding1 in sporen and not verbinding2 in sporen:
            z = station1
            return z
          
   # Als alles al is geweest
    z = stations[0]['Station']
    return z