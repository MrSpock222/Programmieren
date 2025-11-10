#Uebung 1
"""
def Zahlenfolge(n):
    
    while n !=0:
        if n % 3 == 0:
            n = n + 4
            print(n)
        elif n % 4 == 0:
            n = n // 2
            print(n)
        else:
            n = n - 1
            print(n)
Zahlenfolge(50)
"""


#Uebung 2
def Schaltjahr(n):
    schalt = 0
    if n % 4 ==0:
        schalt = 1
    if n %100 == 0:
        schalt = 0
    if n % 400 == 0:
        schalt = 1
    return schalt
print(Schaltjahr(2023))

    

