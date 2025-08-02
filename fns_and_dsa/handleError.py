# try:
#     f = open('main.py')
#     var = bad_var
# except FileNotFoundError:
#     print("Sorry file not found")
# except Exception:
#     print("Sorry, something went wrong")


# try:
#     f = open('fns_and_dsa/main.py')
#     var = bad_var
# except FileNotFoundError as e:
#     print(e)
# except Exception as e:
#     print(e)

try:
    f = open('fns_and_dsa/main.py')
    
except FileNotFoundError as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
    print("Executing Finally...")   
    
# The else runs if no exception is thrown

# The finally runs no matter what happens. Whether the code is successful or an exception is thrown




num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

try:
  divide =  num1/num2
except ZeroDivisionError as e:
    print("Error!", e)
else:
    print(f"{num1} divided by {num2} = {divide}")    


