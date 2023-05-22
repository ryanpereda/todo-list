import json

todo_list = []
todo_list_file = 'todo_list.json'

def add_task(task):
    todo_list.append(task)

def remove_task(task):
    todo_list.remove(task)

def save_task():
    with open(todo_list_file, 'w') as file:
        json.dump(todo_list, file)

def load_task():
    try:
        with open(todo_list_file, 'r') as file:
            tasks = json.load(file)
            return tasks
    except FileNotFoundError:
        return []  # Return an empty list if the file doesn't exist
    except json.JSONDecodeError:
        print("Error: Invalid tasks file format.")
        return []  # Return an empty list if the file format is invalid

class Todo:
    def __init__(self, task, complete="False"):
        self.task = task
        self.complete = complete

    def toggle_task_complete(self):
        self.complete = not self.complete


# add_task("make task")
# save_task()

print(todo_list)
todo_list = load_task()
print(todo_list)


