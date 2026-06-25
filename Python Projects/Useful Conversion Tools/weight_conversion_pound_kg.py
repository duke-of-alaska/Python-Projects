def lb_to_kg(pounds):
    return pounds * 0.453592

def kg_to_lb(kilograms):
    return kilograms * 2.204622

while True:
    choice = input("""
            ==== Select Options ==== 
            
            1. Pounds (lb) to kilograms (kg)
            2. Kilograms (kg) to Pounds (lb)
            3. Exit
                
            Input (in numbers): """)

    if choice == "1":
        weight = float(input("Input the weight in pounds: "))
        result = f"Result: {lb_to_kg(weight)}kg"

    elif choice == "2":
        weight = float(input("Input the weight in kilograms: "))
        result = f"Result: {kg_to_lb(weight)}lb"

    elif choice == "3":
        break

    else:
        print("An error occurred.")

    print(result)