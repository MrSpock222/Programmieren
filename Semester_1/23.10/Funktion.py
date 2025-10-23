#Name(Formalparameterliste) <-signatur (Schnitstellen)
import math
def doit(name):
    print("Funktion.py wurde ausgeführt", name)

doit("Max") #Funktionsaufruf (Aktualparameterliste)

def add(opt1, opt2):
    return opt1 + opt2

s = add(5, 10)
print(s)

def minimum(a, b):
    if a < b:
        return a
    else:
        return b
    
x = 15
y = 25
#minimum(15, 25) <- call-by-value: Aktualparameter werden in die Formalparameter kopiert
print("Minimum ist:", minimum(x, y), "von ", x, "und", y)

def swap(a, b):
    return b, a
s = swap(x, y) #call-by-value
print(s)

def kreisunfang(radius):
    
    umfang = 2 * math.pi * radius
    return umfang
x = kreisunfang(20)
print("Kreisumfang ist:", s)

def zeit(strecke, geschwindigkeit):
    return strecke / geschwindigkeit
y = zeit(1500, 50)
print("Zeit:", s)
o= 50
def kreislauf(x,o):
    return zeit(x,o) 
z = kreislauf(x, o)
print("Kreislaufzeit:", z)

def kw_ps(a):
    return a * 1.35962
print(kw_ps(100))

text = "Fischers Fritze fischt frische Fische, frische Fische fischt Fischers Fritze"

def count_fish(text, wort):
    count = 0
    for char in text:
        if char == wort:
            count += 1
    return count
print(count_fish(text, "f"))
