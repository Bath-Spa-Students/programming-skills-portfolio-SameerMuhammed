# List of sandwich orders
sandwich_orders = ['tuna', 'turkey', 'vegetarian', 'ham and cheese']

# Empty list for finished sandwiches
finished_sandwiches = []

# Loop through sandwich orders
for order in sandwich_orders:
    print(f"I made your {order} sandwich.")
    
    # Move the finished sandwich to the list
    finished_sandwiches.append(order)

# Print a message listing each sandwich that was made
print("\nFinished Sandwiches:")
for sandwich in finished_sandwiches:
    print("- " + sandwich.capitalize())
