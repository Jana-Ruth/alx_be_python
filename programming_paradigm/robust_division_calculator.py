
# numerator = int(input("Enter Numerator: "))
# denominator = int(input("Enter Denominator: "))

# def safe_divide(numerator, denominator):
#     try:
#         num = float(numerator)
#         den = float(denominator)
#         divide = num / den
#     except ZeroDivisionError:
#         print("Error: Cannot divide by zero.")
#     except ValueError:
#         print("Error: Please enter numeric values only.")
#     else:
#         print(f"The value of {numerator} divided by {denominator} is = {divide}")
        
        
def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        den = float(denominator)

        result = num / den
        return f"Result: {result:.2f}"
    
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    
    except ValueError:
        return "Error: Please enter valid numbers."