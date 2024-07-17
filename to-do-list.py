class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self):
        task = input("Enter the task you want to add: ")
        self.tasks.append(task)
        print(f"Task '{task}' added successfully.")

    def remove_task(self):
        try:
            self.view_tasks()
            task_num = int(input("Enter the task number you want to remove: "))
            if 0 <= task_num < len(self.tasks):
                removed_task = self.tasks.pop(task_num)
                print(f"Task '{removed_task}' removed successfully.")
            else:
                print("Invalid task number.")
        except (ValueError, IndexError):
            print("An error occurred. Please enter a valid task number.")

    def view_tasks(self):
        if self.tasks:
            print("Here are your current tasks:")
            for index, task in enumerate(self.tasks):
                print(f"{index}: {task}")
        else:
            print("Your task list is empty.")

    def update_task(self):
        try:
            self.view_tasks()
            task_num = int(input("Enter the task number you want to update: "))
            if 0 <= task_num < len(self.tasks):
                new_task = input("Enter the new task: ")
                old_task = self.tasks[task_num]
                self.tasks[task_num] = new_task
                print(f"Task '{old_task}' updated to '{new_task}' successfully.")
            else:
                print("Invalid task number.")
        except (ValueError, IndexError):
            print("An error occurred. Please enter a valid task number.")

    def display_menu(self):
        print("""
1. Choose 1 to add tasks
2. Choose 2 to remove tasks
3. Choose 3 to view tasks
4. Choose 4 to update tasks
5. Choose 5 to exit
""")

    def run(self):
        print("Welcome to Robo to-do list application")
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")
            if choice == '1':
                self.add_task()
            elif choice == '2':
                self.remove_task()
            elif choice == '3':
                self.view_tasks()
            elif choice == '4':
                self.update_task()
            elif choice == '5':
                print("Exiting the application. Goodbye!")
                break
            else:
                print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    todo_list = ToDoList()
    todo_list.run()
