import math

choice = input("Find the area of circumference or a circle? (a/c) ").lower()
if choice == "a":
    radius = float(input("Enter the radius in cm: "))
    result = math.pi * radius ** 2
    print(f"The area of the circle is {result:.3f}cm.")

elif choice == "c":
    radius = float(input("Enter radius (in cm): "))
    result = 2 * math.pi * radius
    print(f"The circumference is {result:.3f}cm!")

else:
    print("An error occurred.")