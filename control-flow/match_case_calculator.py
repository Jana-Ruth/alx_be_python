num1 = int(input("first number:"))
num2 = int(input("second number:"))
operation = input(" Choose the operation (+, -, *, /):")


match operation:
    case "+":
        print(num1 + num2)
    case "-" :
        print(num1 - num2)   
    case "*":
        print(num1 * num2)    
    case "/":
        print(num1 / num2)   
    case _:
        print("Choose a valid operation")    
        
        
        
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
  print(fruit)
        
        
        
        