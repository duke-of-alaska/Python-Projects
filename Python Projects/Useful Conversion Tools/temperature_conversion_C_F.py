# Temperature Conversion Program

while True:
    choice = input("""
        ==== Temperature Conversion Program ====
        What would you like to do?
        
        1. Convert from Celsius to Fahrenheit
        2. Convert from Fahrenheit to Celsius
        3. Exit
        
        Input (in numbers): """)

    if choice == "1":
        temperature = float(input("Enter temperature (in °C): "))
        calculation = (temperature * 9/5) + 32
        result = f"{temperature}°C = {calculation:.3f}°F"

    elif choice == "2":
        temperature = float(input("Enter temperature (in °F): "))
        calculation = (temperature - 32) * 5/9
        result = f"{temperature}°F = {calculation:.3f}°C"

    elif choice == "3":
        break

    else:
        result = "An error occurred"

    print(result)
