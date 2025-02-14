class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        if not task.strip():  # Check for empty task
            raise ValueError("Task cannot be empty")
        self.tasks.append(task)
        print(f"Task added: {task}")

    def view_tasks(self):
        if not self.tasks:  # Check if tasks list is empty
            print("No tasks available")
        else:
            print("Your tasks:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")

    def update_task(self, task_number, new_task):
        try:
            task_number = int(task_number)
            if task_number < 1 or task_number > len(self.tasks):
                raise ValueError("Invalid task number")
            if not new_task.strip():  # Check for empty new task
                raise ValueError("New task cannot be empty")
            self.tasks[task_number - 1] = new_task
            print(f"Task {task_number} updated")
        except ValueError as e:
            print(f"Error: {e}")

    def delete_task(self, task_number):
        try:
            task_number = int(task_number)
            if task_number < 1 or task_number > len(self.tasks):
                raise ValueError("Invalid task number")
            del self.tasks[task_number - 1]
            print(f"Task {task_number} deleted")
        except ValueError as e:
            print(f"Error: {e}")

def main():
    todo = ToDoList()

    while True:
        print("\nOptions:")
        print("1. Add task")
        print("2. View tasks")
        print("3. Update task")
        print("4. Delete task")
        print("5. Quit")

        try:
            choice = int(input("Choose an option: "))
        except ValueError:
            print("Invalid option. Please enter a number.")
            continue

        if choice == 1:
            task = input("Enter a task: ")
            try:
                todo.add_task(task)
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == 2:
            todo.view_tasks()
        elif choice == 3:
            task_number = input("Enter task number to update: ")
            new_task = input("Enter new task: ")
            try:
                todo.update_task(task_number, new_task)
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == 4:
            task_number = input("Enter task number to delete: ")
            try:
                todo.delete_task(task_number)
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == 5:
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()