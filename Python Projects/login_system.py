import getpass

# Premade account
account_username = "Administrator"
account_password = "1234"
account_recovery_key = "QK023"

welcome = print("""
    ==== Welcome to the Home login system. ====""")

username = input("Enter your username: ")

password = getpass.getpass("Enter your password: ")

recovery_key = input("Do you have a recovery key? (True/False) ").lower()

if recovery_key == "true":
    enter_recovery_key = getpass.getpass("Enter recovery key: ")

    if enter_recovery_key == account_recovery_key:
        print("Succesfully logged in!")

    else:
        print("Sorry, we couldn't log you in.")

elif recovery_key == "false":
    if username == account_username and password == account_password:
        print("Succesfully logged in!")
    else:
        print("Sorry, we couldn't log you in.")

else:
    print("An error occurred.")