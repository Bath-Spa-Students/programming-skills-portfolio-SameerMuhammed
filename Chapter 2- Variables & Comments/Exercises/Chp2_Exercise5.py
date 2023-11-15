
# USB Shopper

# Given values
# budget in pounds
allowance= 50

# price of usb
usb_cost=6

# Calculating the number of usb she can buy
total_usb_sticks=allowance//usb_cost

# Calculating balance
change=allowance%total_usb_sticks

# Printing results
print(f"She is able to afford {total_usb_sticks} usb sticks")
print(f"and her remaining change is {change} POUNDS")
