# function called describe_city()

def describe_city(city, country="Default Country"):
    print(f"{city} is in {country}.")

# Call the function for three different cities
describe_city("Reykjavik", "Iceland")
describe_city("Paris", "France")
describe_city("New York")  # Uses the default country value
