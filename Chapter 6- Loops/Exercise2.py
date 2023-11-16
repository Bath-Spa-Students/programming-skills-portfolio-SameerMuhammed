# Loop to ask users for their age and calculate ticket cost
while True:
    try:
        # Prompt user to enter age
        age = int(input("Enter your age (type '0' to exit): "))

        # Check if the user wants to exit
        if age == 0:
            break

        # Determine ticket cost based on age
        if age < 3:
            ticket_cost = 0
        elif 3 <= age <= 12:
            ticket_cost = 10
        else:
            ticket_cost = 15

        # Print the ticket cost
        print(f"The cost of your movie ticket is ${ticket_cost}\n")
    
    except ValueError:
        print("Invalid input. Please enter a valid age.")
      
