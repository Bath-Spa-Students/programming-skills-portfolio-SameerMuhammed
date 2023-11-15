## Write a Python program to display the current date and time.

# Importing datetime module
import datetime

# getting current date and time
current_datetime = datetime.datetime.now()

# formatting and displaying the date and time
formatted_datetime = current_datetime.strftime("%d/%m/%Y, %H:%M:%S")

print("Current date and time :", formatted_datetime)
