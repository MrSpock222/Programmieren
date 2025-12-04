def groessteAbstandZweierAnananderfolgendenZahlen(n):
    return max([abs(n[i] - n[i+1]) for i in range(len(n)-1)])
print(groessteAbstandZweierAnananderfolgendenZahlen([1, 2, 5, 6, 7, 8, 9, 10]))

def groessteAbstandZweierAnananderfolgendenZahlen1(n):
    groesster = 0
    for i in range(len(n)-1):
        diff = n[i] - n[i+1]
        if diff < 0:
            diff = -diff
        if diff > groesster:
            groesster = diff
    return groesster
print(groessteAbstandZweierAnananderfolgendenZahlen1([1,2,12,-3,6,4]))

