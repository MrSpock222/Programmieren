#Uebung 1

def rad_deg(radiant):
    return radiant * (180/3.14259)
print(rad_deg(50))


#Uebung 2
def palindrom(zahl):
    zahl = abs(int(zahl))
    digits = []
    while zahl > 0:
        
        digits.insert(0, zahl % 10)
        zahl //= 10
    
    if digits == digits[::-1]:
        return True
    else:
        return False
print(palindrom(2323))


#Uebung 3

def primefaktorzerlegung(n):
    primefaktoren = []
    for i in range(2, n+1):
        while n % i == 0:
            primefaktoren.append(i)
            n = n // i
    return primefaktoren
print(primefaktorzerlegung(97))




#Uebung 4
text = "Hallo "
def v_zaehlen(text):
    i = 0
    test = ["a","i","e","o","u"]
    for char in text:
        if char in test:
            i +=1
    return i
print(v_zaehlen(text))