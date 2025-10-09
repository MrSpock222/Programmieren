import random

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

