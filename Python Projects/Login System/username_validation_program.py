# Rules:
# 1. Username must not be more than 12 characters long
# 2. Must not contain spaces
# 3. Must not contain numbers
# 4. Must not contain any special characters

while True:
    username = input("Type in your username: ")
    if len(username) > 12:
        print("Your username cannot be more than 12 characters long!\n")
    elif " " in username:
        print("Your username cannot contain any spaces!\n")
    elif not username.isalpha():
        print("Your username cannot contain digits or special characters!\n")
    else:
        print(f"Welcome {username}!")
        break