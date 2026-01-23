
def umrechnung(value):
    grad = 360/3.14 * value
    return grad
print(umrechnung(1.67))

def palindrom(value):
    digits = []
    while value > 0:
        x = value % 10
        digits.insert(0,x)
        value = value //10
    if digits == digits[::-1]:
        return True
    else:
        return False
print(palindrom(1221))

def primfaktor(value):
    end = []    
    for i in range(2,value +1):
        while value % i == 0:
            end.append(i)
            value //=i
    return end
print(primfaktor(120))


def vokale(text):
    x =0
    for i in text:
        if i in "aeiou":
            x += 1
    return x
print(vokale("Hallo ich bins"))


def zahlenfolge(n):
    while n != 0:
        if n % 3 ==0:
            n+=4
            print(n)
        elif n % 4 == 0:
            n//=2
            print(n)
        else:
            n -=1
            print(n)
zahlenfolge(120)         


def schaltjahr(value):
    x = False
    if value % 4 == 0:
        x = True
    if value % 100 == 0:
        x = False
    if value % 400 == 0:
        x = True
    return x
print(schaltjahr(2012))

def nimm():
    x = 12
    spieler = 1
    row = [5,4,3]
    
    while x !=0:
        a = int(input("Reihe"))
        b = int(input("anzahl"))
        
        row[a-1]-=b
        x= 0
        for i in row:
            x+=i
        if x == 0:
            print(f"Spieler {spieler} gewinnt")
        else:
            spieler =2 if spieler == 1 else 1
nimm()