def min(a):
    kleinste = a[0]
    for i in a:
        if i < kleinste:
            kleinste = i
            return kleinste
print(min([1,5,6,0]))

def minb(b):
    kleinste = b[0]
    for i in range(0,len(b)):
        if b[i] < kleinste:
            kleinste = b[i]
            return kleinste
print(minb([1,5,6,0]))

def minc(c):
    kleinste = c[0]
    i = 0
    while i < len(c):
        if c[i] < kleinste:
            kleinste = c[i]
        i += 1
    return kleinste
print(minc([1,5,6,0]))
