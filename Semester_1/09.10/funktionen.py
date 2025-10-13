import random

def naechstes_level():
    
    print("Wähle einen zahlenbereich immer von 1 ausgehend")
    bereich = int(input())
    print("Denke dir eine zahl zwischen 1 und", bereich, "aus")
    print("Mit g ist die Zahl zu gross, mit k zu klein und mit r richtig")
    t = bereich //2
    print("Ist die Zahl größer als ", t, "? (g/k/r)")

    
    while i != "r":
        i = input()
        if i == "k":
            t = t // 2
            print("Ist die Zahl größer als ", t, "? (g/k/r)")
        elif i == "g":
            if t * 2 >= bereich:
                t = (t + bereich) // 2
                print("Ist die Zahl größer als ", t, "? (g/k/r)")
            else:
                t = t * 2
                print("Ist die Zahl größer als ", t, "? (g/k/r)")
        elif i == "r":
            print("Die Zahl ist ", t)
        else:
            print("Ungültige Eingabe, bitte g, k oder r eingeben.")


def anfang():
    zahl = int(random.randint(1, 10))

    i = 1
    a = int(input("Gib eine Zahl ein: "))
    while a != zahl:
        
        if a < zahl:
            print("Die Zahl ist zu klein")
            i = i + 1
        else:
            print("Die Zahl ist zu gross")
            i = i + 1
        a = int(input("Gib eine Zahl ein: "))
        
    print("Richtig! Du hast", i, "Versuche gebraucht.")