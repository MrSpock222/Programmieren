import test

response = []
# 'wort' wird als Maske für bereits erratene Buchstaben genutzt
wort = None
response = test.ai()


x = list(response)

print("Hangman Game")
print("Das Wort hat", len(response), "Buchstaben.")


# initiale Maske mit Unterstrichen
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
            # finde alle Indexpositionen des geratenen Buchstabens
            indexes = [i for i, c in enumerate(response) if c == guess]
            # setze die Maske an diesen Positionen (keine insert-Operation)
            for index in indexes:
                wort[index] = guess
            # Ausgabe der aktuellen Maske
            for ch in wort:
                print(ch, end=" ")
    else:
        print("Falsch!")
print("Fertig")
        
        






