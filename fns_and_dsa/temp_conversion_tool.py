# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        temp = float(input("Enter the temperature: "))
        unit = input("Is this in Celsius or Fahrenheit? (C/F): ").strip().lower()

        if unit == 'c':
            converted = convert_to_fahrenheit(temp)
            print(f"{temp}°C is {converted:.2f}°F")
        elif unit == 'f':
            converted = convert_to_celsius(temp)
            print(f"{temp}°F is {converted:.2f}°C")
        else:
            raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

    except ValueError as e:
        print(f"Invalid temperature. {e}")

if __name__ == "__main__":
    main()
