import time



while True:
    try:
        timechoice = input("""
        ==== Welcome to the Time Program ====
        What would you like to do?
            
        1. Countdown (per second)
        2. Countdown (notified after finish)
        3. Quit
            
        Input: """)

        if timechoice == "1":
            length = float(input("\nHow long do you want the countdown to be (in minutes)? "))
            seconds = length * 60
            while seconds > 0:
                print(f"Seconds remaining: {seconds}")
                seconds -= 1
                time.sleep(1)
            print("Done!")

        elif timechoice == "2":
            length = float(input("\nHow long do you want the countdown to be (in minutes)? "))
            seconds = length * 60

            while seconds > 0:
                seconds -= 1
                time.sleep(1)
            print("Done!")

        elif timechoice == "3":
            print("Bye!")
            break

        else:
            print("Invald input.")

    except ValueError:
        print("Please input an integer")