print("Nimm-Spiel")

def zeige_spielfeld(reihen):
    print("\nAktueller Spielstand:")
    for i, anzahl in enumerate(reihen, 1):
        print(f"Reihe {i}: " + "O " * anzahl)

row = [5, 4, 3]  
aktueller_spieler = 1
sumrows = sum(row)

while sumrows > 0:
    zeige_spielfeld(row)
    print(f"\nSpieler {aktueller_spieler} ist am Zug")
    
    
    while True:
        try:
            reihe = int(input("Aus welcher Reihe möchtest du Münzen nehmen? (1-3): "))
            if not 1 <= reihe <= 3:
                print("Bitte wähle eine Reihe zwischen 1 und 3!")
                continue
                
            anzahl = int(input("Wie viele Münzen möchtest du nehmen? "))
            if not 1 <= anzahl <= row[reihe-1]:
                print(f"kannst nur 1 bis {row[reihe-1]} Münzen aus dieser Reihe nehmen!")
                continue
                
            break
        except ValueError:
            print("Bitte gebe gültige Zahlen ein!")
            
   
    row[reihe-1] -= anzahl
    sumrows = sum(row)
    
    
    if sumrows == 0:
        print(f"\nSpieler {aktueller_spieler} gewinnt!")
    else:
        
        aktueller_spieler = 2 if aktueller_spieler == 1 else 1