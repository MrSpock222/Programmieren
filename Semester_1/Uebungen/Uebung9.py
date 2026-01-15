data = [
    (0, 430, 15.2),
    (10, 432, 15.4),
    (20, 435, 15.3),
    (30, 438, 15.5),
    (40, 440, 15.4),
    (50, 445, 68.0),     # Fehlerhaft
    (60, 448, 100.5),    # Fehlerhaft
    (70, 450, 15.2),
    (80, 452, 15.4),
    (90, 455, 15.3),
    (100, 455, 70.1),    # Fehlerhaft
    (110, 462, 15.2)
]


def fix_errors(data):
    corrected = []
    valid_velocities = []  
    
    for i in range(len(data)):
        t, h, v = data[i]
        
        if i == 0:
            # Punkt eins, korrekt immer
            corrected.append((t, h, v))
            valid_velocities.append(v)
        else:
            
            height_valid = abs(h - data[i-1][1]) <= 2
            
            
            last_v = corrected[i-1][2]
            velocity_valid = abs(v - last_v) <= 50
            
            if height_valid and velocity_valid:
                # Gültiger Punkt
                corrected.append((t, h, v))
                valid_velocities.append(v)
            else:
                # Fehlerhafter Punkt 
                avg_velocity = sum(valid_velocities) / len(valid_velocities)
                corrected.append((t, h, avg_velocity))
    
    return corrected

data = fix_errors(data)

for entry in data:
    print(f"Zeit: {entry[0]}, Meereshöhe: {entry[1]:.1f}, Geschwindigkeit: {entry[2]:.1f}")   




#Uebung 2:

items = {
    "Filzstift": {"einheiten": 3, "wert_pro_einheit": 1},
    "Füllfeder": {"einheiten": 1, "wert_pro_einheit": 5},
    "Radiergummi": {"einheiten": 40, "wert_pro_einheit": 0.5},
    "Kreide": {"einheiten": 100, "wert_pro_einheit": 0.1}
}

rucksack_groesse = 10

def bepacken_rucksack(items, rucksack_groesse):
    
    # maxi = maximaler Wert
    maxi = [0] * (rucksack_groesse + 1)
    # Speichere Items 
    chosen = [[] for _ in range(rucksack_groesse + 1)]
    
    for item_name, item_data in items.items():
        max_einheiten = item_data["einheiten"]
        wert_pro_einheit = item_data["wert_pro_einheit"]
        
        # Rückwärts durch Rucksackgröße iterieren
        for groesse in range(rucksack_groesse, 0, -1):
            # Versuche bis zu max_einheiten dieses Items hinzuzufügen
            for anzahl in range(1, min(max_einheiten + 1, groesse + 1)):
                if groesse >= anzahl:
                    neuer_wert = maxi[groesse - anzahl] + (anzahl * wert_pro_einheit)
                    if neuer_wert > maxi[groesse]:
                        maxi[groesse] = neuer_wert
                        chosen[groesse] = chosen[groesse - anzahl] + [item_name] * anzahl

    return maxi[rucksack_groesse], chosen[rucksack_groesse]

max_wert, items_gewaehlt = bepacken_rucksack(items, rucksack_groesse)

# Zähle Items
from collections import Counter
items_count = Counter(items_gewaehlt)


print(f"Rucksackgröße: {rucksack_groesse}")
print(f"\nOptimale Bepackung:")
for item, count in sorted(items_count.items()):
    wert_pro_einheit = items[item]["wert_pro_einheit"]
    gesamt_wert = count * wert_pro_einheit
    print(f"  {count}x {item}: {count} Einheiten, {gesamt_wert}€")

print(f"\nGesamtwert: {max_wert}€")

