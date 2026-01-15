

def euclidean_distance(p1, p2):
    """euklidischen Abstand zwischen zwei Punkten"""
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5

def brute_force(points):
    """Abbruchfall: Vergleicht alle Punktpaare wenn <= 3 Punkte"""
    min_dist = float('inf')
    closest_pair = None
    
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            dist = euclidean_distance(points[i], points[j])
            if dist < min_dist:
                min_dist = dist
                closest_pair = (points[i], points[j])
    
    return min_dist, closest_pair

def closest_pair_recursive(px, py):
    
    n = len(px)
    
    # Abbruchfall
    if n <= 3:
        return brute_force(px)
    
    # Teile die Punkte in zwei Hälften
    mid = n // 2
    midpoint = px[mid]
    
    #linke und rechte Hälfte
    pyl = [p for p in py if p[0] <= midpoint[0]]
    pyr = [p for p in py if p[0] > midpoint[0]]
    
    # beide Hälften rekusiv aufruf
    left_dist, left_pair = closest_pair_recursive(px[:mid], pyl)
    right_dist, right_pair = closest_pair_recursive(px[mid:], pyr)
    
    # kleineren Abstand
    if left_dist < right_dist:
        min_dist = left_dist
        closest_pair = left_pair
    else:
        min_dist = right_dist
        closest_pair = right_pair
    
    # Überprüfe Punkte im Streifen
    strip = [p for p in py if abs(p[0] - midpoint[0]) < min_dist]
    
    # Vergleiche alle Paare im Streifen
    for i in range(len(strip)):
        j = i + 1
        while j < len(strip) and (strip[j][1] - strip[i][1]) < min_dist:
            dist = euclidean_distance(strip[i], strip[j])
            if dist < min_dist:
                min_dist = dist
                closest_pair = (strip[i], strip[j])
            j += 1
    
    return min_dist, closest_pair

def closest_pair(points):
   #hauptfunktion
    
    # x-Koordinate
    px = sorted(points, key=lambda p: p[0])
    # y-Koordinate
    py = sorted(points, key=lambda p: p[1])
    
    return closest_pair_recursive(px, py)




points1 = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
dist1, pair1 = closest_pair(points1)
print("Beispiel 1:")
print(f"Punkte: {points1}")
print(f"Nächstes Punktpaar: {pair1}")
print(f"Minimaler Abstand: {dist1:.4f}\n")

 
points2 = [(0, 0), (1, 1), (10, 10), (5, 5), (2, 2), (15, 15), (20, 20)]
dist2, pair2 = closest_pair(points2)
print("Beispiel 2:")
print(f"Punkte: {points2}")
print(f"Nächstes Punktpaar: {pair2}")
print(f"Minimaler Abstand: {dist2:.4f}\n")


points3 = [(0, 0), (1, 0), (2, 0), (100, 100), (101, 100)]
dist3, pair3 = closest_pair(points3)
print("Beispiel 3:")
print(f"Punkte: {points3}")
print(f"Nächstes Punktpaar: {pair3}")
print(f"Minimaler Abstand: {dist3:.4f}")
