def negative_zahlen(n):
    count = 0
    for i in range(len(n)):
        if n[i] < 0:
            count += 1
    print(count)
negative_zahlen([-1, 2, -3, 4, -5, 6, -7, 8, -9, 10])

def negative_zahlen1(n):
    count = 0
    i = 0
    while i < len(n):
        if n[i] < 0:
            count += 1
        i += 1
    print(count)
negative_zahlen1([-1, 2, -3, 4, -5, 6, -7, 8, -9, 10])

def lage_points(p1,p2):
    lage = []
    if p1[0] == p2[0] or p1[1] == p2[1]:
        lage.append("gleich")
    if p1[1] < p2[1]:
        lage.append("Links")
    if p1[1] > p2[1]:
        lage.append("Rechts")
    if p1[0] < p2[0]:
        lage.append("Unten")
    if p1[0] > p2[0]:
        lage.append("Oben")
    distance = ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5
    

    
    return ",".join(lage), distance
print(lage_points((1,2),(2,3)))

    
  
    
    
