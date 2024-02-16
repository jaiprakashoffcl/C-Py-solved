class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})

    def delete_task(self, index):
        del self.tasks[index]

    def mark_task_completed(self, index):
        self.tasks[index]["completed"] = True

    def display_tasks(self):
        print("\nTODO LIST:")
        for i, task in enumerate(self.tasks):
            status = "[x]" if task["completed"] else "[ ]"
            print(f"{i+1}. {status} {task['task']}")

def main():
    todo_list = TodoList()

    while True:
        print("\n1. Add Task\n2. Delete Task\n3. Mark Task Completed\n4. Display Tasks\n5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task: ")
            todo_list.add_task(task)
        elif choice == "2":
            index = int(input("Enter task number to delete: ")) - 1
            todo_list.delete_task(index)
        elif choice == "3":
            index = int(input("Enter task number to mark as completed: ")) - 1
            todo_list.mark_task_completed(index)
        elif choice == "4":
            todo_list.display_tasks()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
          
