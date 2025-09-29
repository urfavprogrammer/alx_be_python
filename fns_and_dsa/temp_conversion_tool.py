
    
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    print(f'{fahrenheit}°F is {celsius}°C')
    return celsius

def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    print(f'{celsius}°C is {fahrenheit}°F')
    return fahrenheit


temp = input("Enter the temperature to convert: ")

if temp.replace('.', '', 1).isdigit() == False:
    print("Invalid temperature. Please enter a numeric value.")
    exit()


unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

if unit == "C":
    convert_to_fahrenheit(float(temp))
elif unit == "F":
    convert_to_celsius(float(temp))
else:
    print("Invalid unit. Please enter C or F.")







