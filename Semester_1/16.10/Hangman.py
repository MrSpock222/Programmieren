import test
i= 0
response = []

wort = None
response = test.ai().lower()


x = list(response)

print("Hangman Game")
print("Das Wort hat", len(response), "Buchstaben.")



if response:
    wort = ["_" for _ in response]
    for _ in response:
        print("_", end=" ")
    
while x != wort:
    guess = input("Gib einen Buchstaben ein: ")
    correct = False
    for char in response:
        if char == guess:
            correct = True
    if correct:
        print("Richtig!")
        if guess in wort:
            print("Diesen Buchstaben hast du bereits erraten.")
        elif response.find(guess) != -1:
            
            indexes = [i for i, c in enumerate(response) if c == guess]
            
            for index in indexes:
                wort[index] = guess
            
            for ch in wort:
                print(ch, end=" ")
    else:
        print("Falsch!")
        for ch in wort:
            print(ch, end=" ")
        
        i += 1
        print("Du hast", i, "von 8 Versuchen verbraucht.")
        if i == 8:
            print("Du hast verloren! Das Wort war:", response)
            break
print("Fertig")
        
        






