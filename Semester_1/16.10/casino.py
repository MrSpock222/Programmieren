import random
from time import sleep
isRunning = True

money = int(input("Aufladen\n"))
while isRunning == True and money > 0:
    print("Du hast",money)
    print("1. Spielen\n2. verlassen")
    command = int(input())
 
    if command == 1:
        einsatz = int(input("Einsatz?\n"))
        isValid = False
        while isValid == False:
            if einsatz > money:
                print("Nicht genug Geld für den Einsatz")
                einsatz = int(input("Einsatz?\n"))
            else:
                isValid = True
        money -= einsatz
        gewinn = einsatz * 2
        print("Möglicher Gewinn",gewinn)
        guess = int(input("Auf was setzt du? 1. grün 2. red 3. black\n"))
        num = random.randint(0,36)
        print("Die Kugel rollt....")
        sleep(1)
        if num == 0:
            print("Grün(0)")
            num = 1
        elif num%2 == 0:
            print("Red(Gerade Zahl)")
            num = 2
        elif num%2 == 1:
            print("Black(Ungerade Zahl)")
            num = 3
        
        if guess == num:
            print("Gewonnen")
            money+= gewinn
            sleep(0.5)
        else:
            print("Verloren")
            sleep(0.5)
 
    elif command == 2:
        isRunning = False
    else:
        print("Error. Try again")
if money <= 0:
    print("Du bist pleite")