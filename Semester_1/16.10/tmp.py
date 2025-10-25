while True:
    guess = input("Gib einen Buchstaben ein: ")
    correct = False
    for char in response:
        if char == guess:
            correct = True
    if correct:
        print("Richtig!")
        for i, char in enumerate(response):
            if char == guess:
                wort.append(guess)
                print(wort, end=" ")
            else:
                print("_", end=" ")
    else:
        print("Falsch!")
for char in response:
    print("_", end=" ")#

def find_indexes(char, wort):
    indexes = []
    for i, c in enumerate(wort):
        if c == char:
            indexes.append(i)
    print(indexes) 


    def palindrom(word):
    a = []
    while word > 0:
        num = word%10
        word//10
        a.append(num)
    for i in range(0, len(a)-i-1):
        if a[i] != a[len(a)-1]:
            return False
    return True
print(palindrom(200))