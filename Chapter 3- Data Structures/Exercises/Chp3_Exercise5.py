
# Original list of people to invite to dinner
guest_list = ['Albert Einstein', 'Ada Lovelace', 'Nelson Mandela']

# Print the name of the guest who can't make it
guest_cant_make_it = 'Nelson Mandela'
print(f"{guest_cant_make_it} can't make it to dinner.\n")

# Replace the guest who can't make it with a new person
new_person = 'Marie Curie'
guest_list[guest_list.index(guest_cant_make_it)] = new_person

# Print a second set of invitation messages
for person in guest_list:
    print(f"Dear {person},\n\tYou are invited to dinner. It would be an honor to have you join us.\n")
