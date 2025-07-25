# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        temp_input = input("Enter the temperature to convert:")
        temp = float(temp_input)
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F):").strip().lower()

        if unit == 'c':
            converted = convert_to_fahrenheit(temp)
            print(f"{temp}°C is {converted:.2f}°F")
        elif unit == 'f':
            converted = convert_to_celsius(temp)
            print(f"{temp}°F is {converted:.2f}°C")
        else:
            raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()

