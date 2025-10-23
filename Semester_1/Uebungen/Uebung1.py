#Uebung 1

def rad_deg(radiant):
    return radiant * (180/3.14259)
print(rad_deg(50))


#Uebung 2
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