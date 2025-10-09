temperature = float(input("Enter the temperature in Celsius: "))

while temperature < 20 or temperature > 42:
   
    if temperature >= 42:
        print("It's to warm.")
        
    elif temperature <= 20:
        print("It's cold.")
    temperature = float(input("Enter the new temperature in Celsius: "))
  
print("It's ok.")