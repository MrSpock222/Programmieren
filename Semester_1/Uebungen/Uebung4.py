#Uebung 1
def ticktactoe():
    reihe1 = ["*", "*", "*"]
    reihe2 = ["*", "*", "*"]
    reihe3 = ["*", "*", "*"]
    print(reihe1)
    print(reihe2)
    print(reihe3)
    
    Spieler1 = True
    Gewonnen = False
    
    while not Gewonnen:
        if Spieler1 == True and Gewonnen == False:
            a = int(input("\nSpieler 1 Welche Reihe?"))
            b = int(input("\nSpieler 1 Welche Spalte?"))
            if a == 1:
                reihe1[b-1] = "X"
            if a == 2:
                reihe2[b-1] = "X"
            if a == 3:
                reihe3[b-1] = "X"
            Spieler1 = False
        print(reihe1)
        print(reihe2)
        print(reihe3)
        for i in range(0,3):
            if reihe1[i] == reihe2[i] == reihe3[i] == "X":
                print("\nSpieler 1 gewinnt!")
                Gewonnen = True
            if reihe1[i] == reihe2[i] == reihe3[i] == "O":
                print("\nSpieler 2 gewinnt!")
                Gewonnen = True
        if reihe1[0] == "X" and reihe1[1] == "X" and reihe1[2] == "X":
            print("\nSpieler 1 gewinnt!")
            Gewonnen = True
        if reihe1[0] == "O" and reihe1[1] == "O" and reihe1[2] == "O":
            print("\nSpieler 2 gewinnt!")
            Gewonnen = True
        if reihe2[0] == "X" and reihe2[1] == "X" and reihe2[2] == "X":
            print("\nSpieler 1 gewinnt!")
            Gewonnen = True
        if reihe2[0] == "O" and reihe2[1] == "O" and reihe2[2] == "O":
            print("\nSpieler 2 gewinnt!")
            Gewonnen = True
        if reihe3[0] == "X" and reihe3[1] == "X" and reihe3[2] == "X":
            print("\nSpieler 1 gewinnt!")
            Gewonnen = True
        if reihe3[0] == "O" and reihe3[1] == "O" and reihe3[2] == "O":
            print("\nSpieler 2 gewinnt!")
            Gewonnen = True
        if reihe1[0] == "X" and reihe2[1] == "X" and reihe3[2] == "X":
            print("\nSpieler 1 gewinnt!")
            Gewonnen = True
        if reihe1[0] == "O" and reihe2[1] == "O" and reihe3[2] == "O":
            print("\nSpieler 2 gewinnt!")
            Gewonnen = True
        if "*" not in reihe1 and "*" not in reihe2 and "*" not in reihe3:
            print("\nUnentschieden!")
            Gewonnen = True
            
        if Spieler1 == False and Gewonnen == False:
            a = int(input("\nSpieler 2 Welche Reihe?"))
            b = int(input("\nSpieler 2 Welche Spalte?"))
            if a == 1:
                reihe1[b-1] = "O"
            if a == 2:
                reihe2[b-1] = "O"
            if a == 3:
                reihe3[b-1] = "O"
            Spieler1 = True
        print(reihe1)
        print(reihe2)
        print(reihe3)
        for i in range(0,3):
            if reihe1[i] == reihe2[i] == reihe3[i] == "X":
                print("\nSpieler 1 gewinnt!")
                Gewonnen = True
            if reihe1[i] == reihe2[i] == reihe3[i] == "O":
                print("\nSpieler 2 gewinnt!")
                Gewonnen = True
        if reihe1[0] == "X" and reihe1[1] == "X" and reihe1[2] == "X":
            print("\nSpieler 1 gewinnt!")
            Gewonnen = True
        if reihe1[0] == "O" and reihe1[1] == "O" and reihe1[2] == "O":
            print("\nSpieler 2 gewinnt!")
            Gewonnen = True
        if reihe2[0] == "X" and reihe2[1] == "X" and reihe2[2] == "X":
            print("\nSpieler 1 gewinnt!")
            Gewonnen = True
        if reihe2[0] == "O" and reihe2[1] == "O" and reihe2[2] == "O":
            print("\nSpieler 2 gewinnt!")
            Gewonnen = True
        if reihe3[0] == "X" and reihe3[1] == "X" and reihe3[2] == "X":
            print("\nSpieler 1 gewinnt!")
            Gewonnen = True
        if reihe3[0] == "O" and reihe3[1] == "O" and reihe3[2] == "O":
            print("\nSpieler 2 gewinnt!")
            Gewonnen = True
        if reihe1[0] == "X" and reihe2[1] == "X" and reihe3[2] == "X":
            print("\nSpieler 1 gewinnt!")
            Gewonnen = True
        if reihe1[0] == "O" and reihe2[1] == "O" and reihe3[2] == "O":
            print("\nSpieler 2 gewinnt!")
            Gewonnen = True
        
        if "*" not in reihe1 and "*" not in reihe2 and "*" not in reihe3:
            print("\nUnentschieden!")
            Gewonnen = True
ticktactoe()

        
            
        
        
    
        
           
    
    


    
    