# List of guests
guests = ['Alice', 'Bob', 'Charlie', 'David']

# Print original invitations
print("Original Invitations:")
for guest in guests:
    print(f"Dear {guest}, you are invited to dinner.")

# Update to mention only two guests can be invited
print("\nUnfortunately, the new dinner table won't arrive in time, and I can invite only two guests for dinner.")

# Use pop() to remove guests until only two names remain
while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Sorry {removed_guest}, I can't invite you to dinner.")

# Print invitations for the two remaining guests
print("\nRemaining Invitations:")
for guest in guests:
    print(f"Dear {guest}, you are still invited to dinner.")

# Use del to remove the last two names
del guests[:]
print("\nList of guests after removing the last two names:", guests)
