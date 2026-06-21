import math

a = float(input("Enter length of side A in cm: "))

b = float(input("Enter length of side B in cm: "))

c = math.sqrt(a**2) + math.sqrt(b**2)

print(f"The hypotenuse (side C) is {c}cm!")