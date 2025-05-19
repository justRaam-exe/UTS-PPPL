from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "done": False})

    def remove_task(self, index):
        return self.tasks.pop(index)

    def mark_as_done(self, index):
        self.tasks[index]["done"] = True

    def mark_as_undone(self, index):
        self.tasks[index]["done"] = False

    def show_tasks(self):
        if not self.tasks:
            print("Tidak ada tugas.")
        for i, t in enumerate(self.tasks):
            status = "✓" if t["done"] else "✗"
            print(f"{i}. [{status}] {t['task']}")


class AddTaskCommand(Command):
    def __init__(self, todo_list, task):
        self.todo_list = todo_list
        self.task = task

    def execute(self):
        self.todo_list.add_task(self.task)

    def undo(self):
        self.todo_list.remove_task(len(self.todo_list.tasks) - 1)


class RemoveTaskCommand(Command):
    def __init__(self, todo_list, index):
        self.todo_list = todo_list
        self.index = index
        self.removed_task = None

    def execute(self):
        self.removed_task = self.todo_list.remove_task(self.index)

    def undo(self):
        self.todo_list.tasks.insert(self.index, self.removed_task)


class MarkAsDoneCommand(Command):
    def __init__(self, todo_list, index):
        self.todo_list = todo_list
        self.index = index

    def execute(self):
        self.todo_list.mark_as_done(self.index)

    def undo(self):
        self.todo_list.mark_as_undone(self.index)


class CommandManager:
    def __init__(self):
        self.undo_stack = []
        self.redo_stack = []

    def execute_command(self, command):
        command.execute()
        self.undo_stack.append(command)
        self.redo_stack.clear()

    def undo(self):
        if self.undo_stack:
            command = self.undo_stack.pop()
            command.undo()
            self.redo_stack.append(command)
        else:
            print("Tidak ada yang bisa di-undo.")

    def redo(self):
        if self.redo_stack:
            command = self.redo_stack.pop()
            command.execute()
            self.undo_stack.append(command)
        else:
            print("Tidak ada yang bisa di-redo.")


# ========== DEMONSTRASI ==========

todo_list = TodoList()
manager = CommandManager()

user_task1 = input("Masukkan Tugas pertama: ")
cmd1 = AddTaskCommand(todo_list, user_task1)
manager.execute_command(cmd1)

user_task2 = input("Masukkan Tugas kedua: ")
cmd2 = AddTaskCommand(todo_list, user_task2)
manager.execute_command(cmd2)

cmd3 = MarkAsDoneCommand(todo_list, 0)
manager.execute_command(cmd3)

print("\nSetelah menambahkan dan menandai selesai:")
todo_list.show_tasks()

print("\nUndo dua langkah:")
manager.undo()
manager.undo()
todo_list.show_tasks()

print("\nRedo satu langkah:")
manager.redo()
todo_list.show_tasks()
