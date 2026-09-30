# Daily to do list manager
tasks = []
while True:
  print(" Daily to do list manager")
  print("1. Add tasks")
  print("2. View tasks")
  print("3. Remove tasks")
  print("4. exit")
  choice = input("Enter your choice:")

  if choice =="1":
    task = input("Enter your task:")
    tasks.append(task)
    print("Add task successfully")
  elif choice =="2":
    if not tasks:
     print("Your task list is empty!")
    else:
     print("Your Tasks")
    for i in range(len(tasks)):
     print(i+1, ".",tasks[i])
  elif choice == "3":
    if not tasks:
     print("Your task list is empty!")
    else:
     for i in range(len(tasks)):
       print(i+1, ".",tasks[i])
     num = int(input("Enter task number to remove: "))
     if num > 0 and num <= len(tasks):
         removed = tasks.pop(num - 1)
         print(removed, "removed successfully")
     else:
      print("Invalid task number!")
  elif choice =="4":
     print("Exiting program. Goodbye!")
     break
  else:
     print ("Invalid choice, please try again.")
    
    
    
    
    
     print("Invalid choice, please try again.")
    
         
     
    