
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
#         print(f"The result of the division is  = {divide}")
        
        
# print(safe_divide(12, 2))


def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        den = float(denominator)
        return f"The result of the division is {num / den}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
