# logical operators, or/and/not

ticket_price_majority = 20
ticket_price_minor = 15

while True:
	try:
		choice = input("""
		==== Welcome to the cinema! ====
		How can we help you today?

		1. Check ticket prices
		2. Order a ticket
		3. Exit

		Input: """)

		if choice == "1":
			print(f"""
		==== PRICING ====
		For 18+: ${ticket_price_majority}
		For minors: ${ticket_price_minor}""")

		elif choice == "2":
			print("	\n	==== PURCHASING TICKETS ====")
			major_q = int(input("	How many tickets (for 18+) do you want to buy? "))
			minor_q = int(input("	How many tickets (for under 18) do you want to buy? "))

			result = (major_q * ticket_price_majority) + (minor_q * ticket_price_minor)

			print(f"	The total is ${result}.")

		elif choice == "3":
			break

		else:
			print("An error occurred.")

	except ValueError:
		print("Please input a valid integer.")

