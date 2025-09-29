FAHRENHEIT_TO_CELSIUS_FACTOR = ""
CELSIUS_TO_FAHRENHEIT_FACTOR = ""

def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    print(f'{fahrenheit}°F is {celsius}°C')
    return celsius

def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    print(f'{celsius}°C is {fahrenheit}°F')
    return fahrenheit

FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

temp = float(input("Enter the temperature to convert: "))
unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

if unit == "C":
    convert_to_fahrenheit(temp)
elif unit == "F":
    convert_to_celsius(temp)
else:
    print("Invalid temperature. Please enter a numeric value.")





