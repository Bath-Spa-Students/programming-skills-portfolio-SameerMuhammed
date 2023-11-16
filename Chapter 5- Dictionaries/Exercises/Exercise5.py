# List of dictionaries representing different pets
pets = [
    {'animal': 'dog', 'owner': 'Alice'},
    {'animal': 'cat', 'owner': 'Bob'},
    {'animal': 'parrot', 'owner': 'Charlie'},
    {'animal': 'rabbit', 'owner': 'David'}
]

# Loop through the list and print information about each pet
for pet in pets:
    print(f"{pet['owner']}'s pet is a {pet['animal']}.")
