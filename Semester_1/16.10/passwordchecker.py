pwd = input("Passwort eingeben: ")


for char in pwd:
    if char.isupper():
        upper = True
    elif char.islower():
        lower = True
    elif char.isdigit():
        digit = True
    else:
        symbol = True
if len(pwd) >= 8 <= 12 and upper and lower and digit and symbol:
    print("Password ist korrekt")
else:
    print("Password ist inkorrekt")

