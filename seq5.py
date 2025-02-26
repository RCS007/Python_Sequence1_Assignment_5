# Write a Python program that requests from the user a temperature in degrees Fahrenheit,
# and displays the equivalent temperature in degrees Celsius. (Hint : 100 degree Fahrenheit
# is equal to 37.8 degree Celsius)

# Input temperature in Fahrenheit
fahrenheit = float(input("Enter temperature in Fahrenheit: "))

# Convert to Celsius using the formula
celsius = (fahrenheit - 32) * 5 / 9

# Display the result
print(f"{fahrenheit}°F is equal to {celsius:.2f}°C.")
