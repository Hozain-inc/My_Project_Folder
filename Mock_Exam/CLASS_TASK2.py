from pathlib import Path
workspace = Path("Mock_Exam")
workspace.mkdir(exist_ok = True)
file_path = workspace / "notes.txt"

with open(file_path, "w", encoding = "utf-8") as f:
  f.write("file_path")




tasks = []


while True:
    task1 = input("Enter today's task: ")
    task2 = input("Enter today's task: ")
    task3 = input("Enter today's task: ")
    tasks.append(task1)
    tasks.append(task2)
    tasks.append(task3)
    print(f"{task1}, {task2}, {task3} has been added successfully. ")
    remove = input("Do you want to remove a task? (yes/no): ")
    if remove == 'yes':
        remove_task = input("Enter the task you want to remove: ")
        if remove_task in tasks:
            tasks.remove(remove_task)
            print(f"{remove_task} has been removed")
        else:
            print(f"{remove_task} doesn't exist")
            break
    else:
        print(tasks)
        break
         





















