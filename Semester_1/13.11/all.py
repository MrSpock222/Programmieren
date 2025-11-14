import trinkitrinki

n = int(input("Gebe Zahl ein\n"))

a,b = trinkitrinki.sieb(n)
x,y = trinkitrinki.brute(n)
t,z = trinkitrinki.siebneu(n)



print("Ergebnis: sieb: ", a, " brute: ", x," \n Zeit: sieb: ",b, " brute: ",y , " siebneu: ",z  )