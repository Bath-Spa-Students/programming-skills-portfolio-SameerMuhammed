# Initialize an empty list to store pizza toppings
pizza_toppings = []

# Prompt the user to enter pizza toppings
while True:
    topping = input("Enter a pizza topping (type 'quit' to finish): ")
    
    # Check if the user wants to quit
    if topping.lower() == 'quit':
        break
    
    # Add the topping to the list and print a message
    pizza_toppings.append(topping)
    print(f"Adding {topping} to your pizza.")

# Print the final list of pizza toppings
print("\nYour pizza will have the following toppings:")
for topping in pizza_toppings:
    print("- " + topping)

