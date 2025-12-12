#Wunschliste 

#1 =  neuer Wunsch

#2 = Liste anzeigen

#3 = Gesamtpreis anzeigen

#Wenn 1, dann fragen nach Name und Wunsch und Preis

#Wenn 2, dann alle Wünsche mit Preisen anzeigen, nach namen soritert

#3 = Gesamtpreis aller Wünsche anzeigen

wunschliste = []
pfad = r"X:\Github\Programmieren\Semester_1\11.12\wunschliste.txt"
try: 
    with open(pfad, "r") as datei:
        for zeile in datei:
            zeile = zeile.strip()
            if zeile: 
                name, wunsch, preis = zeile.split("||")
                wunschliste.append((name.strip(), wunsch.strip(), float(preis)))
except FileNotFoundError:
    pass
def neuer_wunsch(name, wunsch, preis):
    
    existiert = False
    for i, eintrag in enumerate(wunschliste):
        if eintrag[0] == name:
            wunschliste[i] = (name, f"{eintrag[1]}, {wunsch}", eintrag[2] + float(preis))
            existiert = True
            break
    
    if not existiert:
        wunschliste.append((name, wunsch, float(preis)))
    
    
    pfad = r"X:\Github\Programmieren\Semester_1\11.12\wunschliste.txt"
    with open(pfad, "w") as datei:
        for eintrag in wunschliste:
            datei.write(f"{eintrag[0]}||{eintrag[1]}||{float(eintrag[2])}\n")
def liste_anzeigen():
    for eintrag in sorted(wunschliste):
        print(f"Name: {eintrag[0]}, Wunsch: {eintrag[1]}, Preis: {eintrag[2]} Euro")
def gesamtpreis_anzeigen():
    gesamtpreis = sum(eintrag[2] for eintrag in wunschliste)
    print(f"Gesamtpreis aller Wünsche: {gesamtpreis} Euro")
while True:
    print("Wunschliste Menü:")
    print("1 = Neuer Wunsch")
    print("2 = Liste anzeigen")
    print("3 = Gesamtpreis anzeigen")
    print("4 = Beenden")
    auswahl = input("option: ")
    if auswahl == "1":
        name = input("Namen ")
        wunsch = input("Wunsch ")
        preis = float(input("Preis "))
        neuer_wunsch(name, wunsch, preis)
    elif auswahl == "2":
        liste_anzeigen()
    elif auswahl == "3":
        gesamtpreis_anzeigen()
    elif auswahl == "4":
        break
    else:
        print("Ungültige Auswahl, erneut versuchen.")
    
    