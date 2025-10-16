import funktionen

print("Willkommen zum Zahlraten-Spiel!")
print("Welchen Modus möchtest du spielen?")
print("1. Normal")
print("2. Reverse")
print()
while True:
    modus = input("Gib 1 oder 2 ein: ")
    if modus == "1":
        funktionen.anfang()
        break
    elif modus == "2":
        funktionen.naechstes_level()
        break
    else:
        print("Ungültige Eingabe, bitte 1 oder 2 eingeben.")
        

    








  

