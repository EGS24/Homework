# Задача 1. Стек
# Мы уже говорили, что в программировании нередко необходимо создавать
# свои собственные структуры данных на основе уже существующих. Одним
# из таких “базовых” структур является стек.
# Стек - это абстрактный тип данных, представляющий собой список
# элементов, организованных по принципу LIFO (англ. last in — first out,
# «последним пришёл — первым вышел»).
# Простой пример: стек из книг на столе. Единственной книгой, чья обложка
# видна, является самая верхняя. Чтобы получить доступ к, например, третьей
# снизу книге, нам нужно убрать все книги, лежащие сверху, одну за другой.
# Напишите класс, который реализует Стек и его возможности (достаточно
# будет добавления и удаления элемента).

# После этого напишите ещё один класс “Менеджер задач”. В менеджере
# задач можно выполнить команду “новая задача”, в которую передаётся сама
# задача (str) и её приоритет (int). Сам менеджер работает на основе Стэка (не
# наследование!). При выводе менеджера в консоль все задачи должны быть
# отсортированы по приоритету: чем меньше число, тем выше задача.
# Вот пример основной программы:
# manager = TaskManager()
# manager.new_task("сделать уборку", 4)
# manager.new_task("помыть посуду", 4)
# manager.new_task("отдохнуть", 1)
# manager.new_task("поесть", 2)
# manager.new_task("сдать дз", 2)
# print(manager)
# Результат:<br>
# 1 отдохнуть<br>
# 2 поесть; сдать дз<br>
# 4 сделать уборку; помыть посуду<br>
# Дополнительно: реализуйте также удаление задач и подумайте, что делать
# с дубликатами

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def __str__(self):
        return str(self.items)


class TaskManager:
    def __init__(self):
        self.stack = Stack()

    def new_task(self, task: str, priority: int):  # удаляю задачу по приоритету
        if (task, priority) in self.stack.items:  # убираю дубликат, если задачи и приоритет совпадают уже в стеке
            return
        self.stack.push((task, priority))

    def remove_task(self, task: str, priority: int):  # удаляю задачу по задаче и приоритету
        new_stack = Stack()
        while not self.stack.is_empty():
            item = self.stack.pop()
            if (task, priority) != item:
                new_stack.push(item)

        while not new_stack.is_empty():
            self.stack.push(new_stack.pop())

    def remove_task_full(self, task: str):  # удаляю полностью задачу, из всех приоритетов
        new_stack = Stack()
        while not self.stack.is_empty():
            item = self.stack.pop()
            if task != item[0]:
                new_stack.push(item)

        while not new_stack.is_empty():
            self.stack.push(new_stack.pop())

    def remove_all_tasks(self):  # удаляю все задачи
        while not self.stack.is_empty():
            self.stack.pop()

    def __str__(self):
        if self.stack.is_empty():
            return "Стек задач пустой!"
        tasks_dict = {}
        new_stack = Stack()

        while not self.stack.is_empty():
            task, priority = self.stack.pop()
            new_stack.push((task, priority))
            if priority in tasks_dict:
                tasks_dict[priority].append(task)
            else:
                tasks_dict[priority] = [task]  # список задач

        while not new_stack.is_empty():
            # добавил в новый стек все элементы, и обратно в старый, чтобы он остался,
            # когда из него все элементы удалятся в словарь,
            # и чтобы он не оказался в итоге пустым для последующих операций
            self.stack.push(new_stack.pop())

        tasks_str = ""
        for priority in sorted(tasks_dict.keys()):
            tasks_str += f"{priority} {'; '.join(tasks_dict[priority])}\n"
        return tasks_str


if __name__ == "__main__":
    manager = TaskManager()
    manager.new_task("сделать уборку", 1)
    manager.new_task("сделать уборку", 2)
    manager.new_task("помыть посуду", 4)
    manager.new_task("сделать уборку", 3)
    manager.new_task("отдохнуть", 1)
    manager.new_task("поесть", 2)
    manager.new_task("сдать дз", 2)
    print(manager)
    manager.remove_task("сделать уборку", 3)
    print(manager)
    manager.remove_task_full("сделать уборку")
    print(manager)
    manager.remove_all_tasks()
    print(manager)
