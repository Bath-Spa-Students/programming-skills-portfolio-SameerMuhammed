# Dictionary of major rivers and the countries they run through
major_rivers = {
    'nile': 'Egypt',
    'amazon': 'Brazil',
    'yangtze': 'China'
}

# Print a sentence about each river
print("Rivers and Countries:")
for river, country in major_rivers.items():
    print(f"The {river.capitalize()} runs through {country}.")

# Print the name of each river
print("\nRivers:")
for river in major_rivers.keys():
    print(river.capitalize())

# Print the name of each country
print("\nCountries:")
for country in major_rivers.values():
    print(country)
