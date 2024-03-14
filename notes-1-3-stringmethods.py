# Methods (Strings)
# Author: Ubial
# 22 February 2024

# Ask the user what is the weather like
weather = input("What's the weather like? ")

# If they reply rainy
# Bring an umbrella
if weather.lower().strip("!.?, ") == "rainy":
    print("You'll need an umbrella! ☂️")
else:
    print(f"Sorry, I don't understand {weather}.")
