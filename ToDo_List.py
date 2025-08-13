################## Variables ###################

todo_list = []
choice_options = [1, 2, 3]

################## While Loop ##################

while True:
  choice = ""

  if not todo_list:
    print("Your ToDo list is empty")
  else:
    index = 1
    for task in todo_list:
      print(f"{index}. {task}")
      index += 1

################# Choices ######################

  if choice == "":
    print()
    print("Options:")
    print("1) Add Task")
    print("2) Remove Task")
    print("3) Quit")
    print()
    choice = input()
    if choice not in choice_options:
      print("Please select proper option (1, 2, or 3)")

  else:
    break

################ ToDo List #####################

  if choice == "1":
    new_task = input("Please enter a task you would like to add to the ToDo list: ")
    print("Adding task")
    todo_list.append(new_task)
    print(f"Task '{new_task}' added to the ToDo list")
    print()

  elif choice == "2":
    if len(todo_list) == 0:
      print("Todo list is currently empty")
    else:
      print("Removing task")
      todo_list.pop()

  elif choice == "3":
    print("Quitting")
    break
