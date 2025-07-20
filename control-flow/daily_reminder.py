# message = "Hello, world!"

# for character in message:
#   print("character", character)
  
  
# for number in range(1, 6):
#   print("attempt", number, (number+1)* "."
# ran = range(1,4)
# print(ran)
  
task = input("Input a task description ")
priority = input("is task priority high, medium, low ")
time_bound = input("Is task time-bound: yes or no ")


match priority:
    case "high":
        print(task, "is a high priority task")
    case "medium":
        print(task, "is a medium priority task")
    case "low":
        print(task, "is a low priority task")
        
if time_bound == "yes" :
    print("task that requires immediate attention today!")    
else:
    print(". Consider completing it when you have free time.")  
    
