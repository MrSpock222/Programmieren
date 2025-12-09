def ez(z, N):
	s = 0.0
	fact = 1  # k!
	pwr = 1.0  # z**k
	for k in range(N):
		if k > 0:
			fact *= k
			pwr *= z
		s += pwr / fact
	return s
print(ez(2, 10))





def MatchingOhneBreak(persons, pairs):
    
    
    gruppe_AB = []
    gruppe_AC = []
    gruppe_BC = []
    pairs = [] 

    # 2. Personen einsortieren
    FÜR jede person IN persons:
        WENN person.skills == {"A", "B"}:
            gruppe_AB.append(person)
        WENN person.skills == {"A", "C"}:
            gruppe_AC.append(person)
        WENN person.skills == {"B", "C"}:
            gruppe_BC.append(person)

    
    # matchen Gruppe AB mit Gruppe AC
    
    SOLANGE (Länge(gruppe_AB) > 0 UND Länge(gruppe_AC) > 0):
        person1 = gruppe_AB.remove_letztes()
        person2 = gruppe_AC.remove_letztes()
        pairs.append((person1, person2))

    # Falls noch ABs übrig sind, matchen mit BC
    SOLANGE (Länge(gruppe_AB) > 0 UND Länge(gruppe_BC) > 0):
        person1 = gruppe_AB.remove_letztes()
        person2 = gruppe_BC.remove_letztes()
        pairs.append((person1, person2))

    # Falls noch ACs und BCs übrig sind matchen 

    SOLANGE (Länge(gruppe_AC) > 0 UND Länge(gruppe_BC) > 0):
        person1 = gruppe_AC.remove_letztes()
        person2 = gruppe_BC.remove_letztes()
        pairs.append((person1, person2))

    return pairs









class Punkt:
    x: Zahl
    y: Zahl

class Rechteck:
    x_min: Zahl  (linker Rand)
    x_max: Zahl  (rechter Rand)
    y_min: Zahl  (unterer Rand)
    y_max: Zahl  (oberer Rand)

def IstPunktImRechteck(punkt, rechteck):
  
    
    # Prüfen der X-Koordinate
    innerhalb_x = (punkt.x >= rechteck.x_min) and (punkt.x <= rechteck.x_max)
    
    # Prüfen der Y-Koordinate
    innerhalb_y = (punkt.y >= rechteck.y_min) and (punkt.y <= rechteck.y_max)
    
    
    WENN (innerhalb_x UND innerhalb_y):
        return True
    SONST:
        return False
    

class Kreis:
    center: Punkt (hat x, y)
    radius: Zahl

dev IstPunktImKreis(punkt, kreis):
   
    
    # Abstand auf der X-Achse und Y-Achse berechnen
    dx = punkt.x - kreis.center.x
    dy = punkt.y - kreis.center.y
    
    # Quadrierte Distanz berechnen (Satz des Pythagoras a² + b² = c²)
    distanz_quadrat = (dx * dx) + (dy * dy)
    
    # Radius quadrieren zum Vergleich
    radius_quadrat = kreis.radius * kreis.radius
    
    
    WENN (distanz_quadrat <= radius_quadrat):
        return True  
    SONST:
        return False