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
        if 0 <= self.index < len(self.todo_list.tasks):
            self.removed_task = self.todo_list.remove_task(self.index)
        else:
            print("Index tidak valid")
            
    def undo(self):
        if self.removed_task:
            self.todo_list.tasks.insert(self.index, self.removed_task)


class MarkAsDoneCommand(Command):
    def __init__(self, todo_list, index):
        self.todo_list = todo_list
        self.index = index

    def execute(self):
        if 0 <= self.index < len(self.todo_list.tasks):
            self.todo_list.mark_as_done(self.index)
        else:
            print("index tidak valid")

    def undo(self):
        if 0 <= self.index < len(self.todo_list.tasks):
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

# todo_list = TodoList()
# manager = CommandManager()

# user_task1 = input("Masukkan Tugas pertama: ")
# cmd1 = AddTaskCommand(todo_list, user_task1)
# manager.execute_command(cmd1)

# user_task2 = input("Masukkan Tugas kedua: ")
# cmd2 = AddTaskCommand(todo_list, user_task2)
# manager.execute_command(cmd2)

# cmd3 = MarkAsDoneCommand(todo_list, 0)
# manager.execute_command(cmd3)

# print("\nSetelah menambahkan dan menandai selesai:")
# todo_list.show_tasks()

# print("\nUndo dua langkah:")
# manager.undo()
# manager.undo()
# todo_list.show_tasks()

# print("\nRedo satu langkah:")
# manager.redo()
# todo_list.show_tasks()


def main():
    todo_list = TodoList()
    manager = CommandManager()
    
    while True:
        print("===========================")
        print("Todo List Program :")
        print("1. Add task")
        print("2. Remove task")
        print("3. Mark task as done")
        print("4. Undo")
        print("5. Redo")
        print("6. Show tasks")
        print("7. Exit")
        print("===========================")
        
        input_choice = input("Pilih Menu : ")
        
        if input_choice == "1":
            task_adding = input("Masukkan Tugas : ")
            cmd = AddTaskCommand(todo_list, task_adding)
            manager.execute_command(cmd)
        elif input_choice == "2":
            todo_list.show_tasks()
            try:
                idx = int(input("Masukkan Index Tugas yang ingin dihapus :"))
                cmd = RemoveTaskCommand(todo_list, idx)
                manager.execute_command(cmd)
            except ValueError:
                print("Indeks tidak valid")
        elif input_choice == "3":
            todo_list.show_tasks()
            try:
                idx = int(input("Masukkan Index Tugas yang ingin ditandai selesai : "))
                cmd = MarkAsDoneCommand(todo_list, idx)
                manager.execute_command(cmd)
            except ValueError:
                print("Indeks tidak valid")
        elif input_choice == "4":
            manager.undo()
        elif input_choice == "5":
            manager.redo()
        elif input_choice == "6":
            todo_list.show_tasks()
        elif input_choice == "7":
            print("Terima Kasih ^_^")
            break
        else:
            print("Pilihan tidak valid, silahkan running ulang program")
            
if __name__ == "__main__":
    main()