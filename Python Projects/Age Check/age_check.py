# Age Check Program
print("Hello!")

try:
    age = int(input("Enter your current age: "))
    if 13 <= age < 18:
        print("Welcome! Some restrictions have been applied to you due to your age.")

    elif age >= 18:
        print("Welcome!")

    elif 0 < age < 13:
        print("Sorry, you may not sign up yet.")

    else:
        print("An error occurred.")

except ValueError:
    print("Please input an integer.")