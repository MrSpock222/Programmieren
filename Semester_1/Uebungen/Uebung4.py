#Uebung 1
def ticktactoe():
    reihe1 = []
    reihe2 = []
    reihe3 = []
    
    a = input("\nWelche Reihe?")
    b = input("Welche Spalte?")
    
    n = "X"
    
    if a == "1": 
        if b == "1":
            n = "X" if n == "O" else "O"
            reihe1.insert(0, n)
        print(reihe1)
        
        
    if a == "2":
        if b == "2":
            n = "X" if n == "O" else "O"
            reihe2.insert(1, n)

        print(reihe2)
    if a == "3":
        if b == "3":
            n = "X" if n == "O" else "O"
            reihe3.insert(2, n)
        print(reihe3)


    
    
    
ticktactoe()