print("Hello!")

while True:
    try:
        age = int(input("Enter your current age: "))

        if age < 1 or age > 120:
            print("That doesn't seem like a real age. Please try again.")
            continue 

        if 13 <= age < 18:
            print("Welcome! Some restrictions have been applied to you due to your age.")
            break 

        elif age >= 18:
            print("Welcome!")
            break 

        elif 0 < age < 13:
            print("Sorry, you may not sign up yet.")
            break

        else:
            print("An error occurred. Please enter a valid age.")

    except ValueError:
        print("Please input an integer.")