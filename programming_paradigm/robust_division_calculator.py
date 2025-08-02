
numerator = int(input("Enter Numerator: "))
denominator = int(input("Enter Denominator: "))

def safe_divide(numerator, denominator):
    try:
       divide = numerator / denominator
    except ZeroDivisionError as e:
        print("Error!", e)
    except ValueError as e:
        print("Error!", e)
    else:
        print(f"The value of {numerator} divided by {denominator} is = {divide}")
        
print(safe_divide(numerator, denominator))