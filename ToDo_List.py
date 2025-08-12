################## Variables ###################

todo_list = ["brush teeth", "brush hashbrown"]

while True:
  new_task = input("Enter the task: ")

########### Append new task to list ############

  todo_list.append(new_task)

########### Check if list is empty #############

  if len(todo_list) == 0:
    print("Your ToDo list is empty")
  
########### Iterate through list ###############

  else:
    index = 1
    for task in todo_list :
      print(f"{index}.{task}")
      index += 1
  print()
