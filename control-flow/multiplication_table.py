x = int(input("Enter a number to see its multiplication table:"))


for number in range(1, 11):
   print(f"{number} * {x} = {number * x}")
    
def calculate_area(length, width):
    """Calculates the area of a rectangle."""
    area = length * width
    print(area)
calculate_area(5,10)

