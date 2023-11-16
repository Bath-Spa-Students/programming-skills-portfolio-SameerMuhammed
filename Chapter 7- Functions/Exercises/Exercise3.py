# function called make_shirt()
def make_shirt(size, message):
    print(f"Making a {size}-sized shirt with the message: '{message}'.")

# Call the function using positional arguments
make_shirt("medium", "Hello, World!")

# Call the function using keyword arguments
make_shirt(size="large", message="Python is awesome!")
