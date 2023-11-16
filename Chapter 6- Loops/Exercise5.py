
# List of sandwich orders with 'pastrami' appearing at least three times
sandwich_orders = ['tuna', 'pastrami', 'turkey', 'pastrami', 'vegetarian', 'ham and cheese', 'pastrami']

# Empty list for finished sandwiches
finished_sandwiches = []

# Print a message about running out of pastrami
print("Sorry, we've run out of pastrami.")

# Remove all occurrences of 'pastrami' from sandwich_orders using a while loop
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

# Loop through sandwich orders
for order in sandwich_orders:
    print(f"I made your {order} sandwich.")
    
    # Move the finished sandwich to the list
    finished_sandwiches.append(order)

# Print a message listing each sandwich that was made
print("\nFinished Sandwiches:")
for sandwich in finished_sandwiches:
    print("- " + sandwich.capitalize())
    
