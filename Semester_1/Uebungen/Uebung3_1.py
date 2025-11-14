
#Uebung 2

def TagJahr(date):
    tage = {"jan":0, "feb":31, "mar":59, "apr":90, "mai":120, "jun":151, "jul":181, "aug":212, "sep":243, "okt":273, "nov":304, "dez":334}
    error= {"jan":31, "feb":28, "mar":31, "apr":30, "mai":31, "jun":30, "jul":31, "aug":31, "sep":30, "okt":31, "nov":30, "dez":31}
    day,month,year = date.split()
    
    year = int(year)
    

    x = tage[month]
    z = error[month]
    z = int(z)
    day = int(day)

    schalt = 0
    if year % 4 ==0:
        schalt = 1
    if year %100 == 0:
        schalt = 0
    if year % 400 == 0:
        schalt = 1
    
    if schalt == 1 and month == "feb" and day == 29:
        y = int(day) + x
        return print(y)
    
    if z < day:
        return print("error")

    if schalt == 1:
        y = int(day) + x +1
        return print(y)
    
    else:
        y = int(day) + x
        return print(y)
    

TagJahr("29 feb 2004")



#Uebung 1:

# Zur Multiplikation von zweier Zahlen
"""
1. Man halbiert die linke Zahl (Multiplikator) immer weiter, bis man bei 1 ankommt, während man die rechte Zahl (Multiplikand) gleichzeitig verdoppelt.

2. Man streicht alle Zeilen, in denen die linke Zahl gerade ist.

3. Die Summe der übrigen (nicht gestrichenen) Zahlen auf der rechten Seite ergibt das korrekte Produkt.
"""

def russianmulti(m,n):
    
    tmp=[]
    y = n
    while m !=1:
        n = n + n
        m = m //2
        if m % 2 !=0:
            tmp.append(n)
    for i in tmp:
        y = y + i 
    return print (y)

russianmulti(27,82)



#Uebung 3:
def lokalMinimaMaxima(n):

    minima = []
    maxima = []
    for i in range(1,len(n)-1):
        if n[i] < n[i-1] and n[i] < n[i+1]:
            minima.append(n[i])
        if n[i] > n[i-1] and n[i] > n[i+1]:
            maxima.append(n[i])
    print("Minima: ", minima)
    print("Maxima: ", maxima)
    
lokalMinimaMaxima([1,3,5,4,6,5,1,2,1,1])


#Uebung 4:
def arithmeticMean():
    values = [3,5,7,8,1,-1,4,0]
    x = sum(values)
    y = x/len(values)
    
    minimum = min(values)
    maximum = max(values)
    
    return print (y, minimum, maximum)
arithmeticMean()

def arithmeticMean1():
    values = [3,5,7,8,1,-1,4,0]
    x = 0
    y = 0
    minimum = values[0]
    maximum = values[0]
    for i in values:
        x = x + i
    y = x/len(values)
    
    for j in values:
        if j < minimum:
            minimum = j
    
    for l in values:
        if l > maximum:
            maximum = l
    
    return print(y,minimum,maximum)
arithmeticMean1()