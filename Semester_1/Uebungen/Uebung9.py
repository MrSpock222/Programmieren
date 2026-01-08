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
    # Identifiziere valide Punkte (Änderung <= 2)
    valid_indices = [0]  # Erster ist immer valid
    for i in range(1, len(data)):
        if abs(data[i][1] - data[i-1][1]) <= 2:
            valid_indices.append(i)
    
    corrected = data[:]
    for i in range(len(data)):
        if i not in valid_indices:
            # Finde nächsten validen vorher und nachher
            prev_i = max([j for j in valid_indices if j < i], default=None)
            next_i = min([j for j in valid_indices if j > i], default=None)
            if prev_i is not None and next_i is not None:
                prev_t, prev_h, prev_v = data[prev_i]
                next_t, next_h, next_v = data[next_i]
                curr_t = data[i][0]
                # Lineare Interpolation
                factor = (curr_t - prev_t) / (next_t - prev_t)
                h = prev_h + (next_h - prev_h) * factor
                v = prev_v + (next_v - prev_v) * factor
                corrected[i] = (curr_t, h, v)
    return corrected

data = fix_errors(data)

for entry in data:
    print(f"Zeit: {entry[0]}, Meereshöhe: {entry[1]:.1f}, Geschwindigkeit: {entry[2]:.1f}")   
