

text = "Dieses da ist es"
pattern = "es"

def patternfind(text, pattern, case_sensitive=True):
    indices = []
    index = 0
    if not case_sensitive:
        text_cmp = text.lower()
        pattern_cmp = pattern.lower()
    else:
        text_cmp = text
        pattern_cmp = pattern

    while index <= len(text_cmp) - len(pattern_cmp):
        if text_cmp[index:index + len(pattern_cmp)] == pattern_cmp:
            indices.append(index)
            index += len(pattern_cmp)
        else:
            index += 1
    return indices
        
print(patternfind(text, "Es", case_sensitive=False))