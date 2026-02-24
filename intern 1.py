tasks = []

def show_menu():
    print("\n===== TO-DO LIST =====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Mark Task as Done")
    print("5. Exit")

def view_tasks():
    if not tasks:
        print("No tasks yet!")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            status = "✓" if task["done"] else "✗"
            print(f"{i}. [{status}] {task['name']}")

def add_task():
    name = input("Enter task: ")
    tasks.append({"name": name, "done": False})
    print(f"'{name}' added!")

def delete_task():
    view_tasks()
    num = int(input("Enter task number to delete: ")) - 1
    removed = tasks.pop(num)
    print(f"'{removed['name']}' deleted!")

def mark_done():
    view_tasks()
    num = int(input("Enter task number to mark as done: ")) - 1
    tasks[num]["done"] = True
    print(f"'{tasks[num]['name']}' marked as done!")

while True:
    show_menu()
    choice = input("Choose (1-5): ")

    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        mark_done()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")
