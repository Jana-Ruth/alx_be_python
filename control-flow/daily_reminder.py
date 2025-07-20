# message = "Hello, world!"

# for character in message:
#   print("character", character)
  
  
# for number in range(1, 6):
#   print("attempt", number, (number+1)* "."
# ran = range(1,4)
# print(ran)
  
task = input("Enter your task: ")
time_bound = input("Is it time-bound? (yes/no): ")
priority = input("Priority (high/medium/low): ")



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
    
print(f"Reminder: You have a '{task}' task with {priority} priority. Time-bound: {time_bound}.")