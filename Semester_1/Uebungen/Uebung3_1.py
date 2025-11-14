def TagJahr(date):
    tage = {"jan":0, "feb":31, "mar":59, "apr":89, "mai":120, "jun":150, "jul":181, "aug":212, "sep":242, "okt":273, "nov":303, "dez":334}
    error= {"jan":31, "feb":28, "mar":31, "apr":30, "mai":31, "jun":30, "jul":31, "aug":31, "sep":30, "okt":31, "nov":30, "dez":31}
    day,month,year = date.split()
    
    year = int(year)
    

    x = tage[month]
    z = error[month]

    schalt = 0
    if year % 4 ==0:
        schalt = 1
    if year %100 == 0:
        schalt = 0
    if year % 400 == 0:
        schalt = 1
    
    if z < day:
        return print("error")
        
        

    if schalt == 1:
        y = int(day) + x +1
    else:
       y = int(day) + x 
    
    

    

TagJahr("1 feb 2005")