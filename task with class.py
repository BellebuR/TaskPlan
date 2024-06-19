from datetime import datetime


class Task:
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date
        self.is_completed = False

    def mark_as_completed(self):
        self.is_completed = True

    def __str__(self):
        status = 'Выполнено' if self.is_completed else 'Не выполнено'
        return f"Задача: {self.description}, Срок: {self.due_date}, Статус: {status}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, due_date):
        task = Task(description, due_date)
        self.tasks.append(task)

    def mark_task_as_completed(self, description):
        for task in self.tasks:
            if task.description == description:
                task.mark_as_completed()
                break

    def get_current_tasks(self):
        return [task for task in self.tasks if not task.is_completed]

    def __str__(self):
        if not self.tasks:
            return "Нет задач"
        return "\n".join(str(task) for task in self.tasks)


# Пример использования
if __name__ == "__main__":
    manager = TaskManager()
    manager.add_task("Купить продукты", "2023-10-15")
    manager.add_task("Подготовить отчет", "2023-10-20")

    print("Все задачи:")
    print(manager)

    manager.mark_task_as_completed("Купить продукты")

    print("\nТекущие задачи:")
    for task in manager.get_current_tasks():
        print(task)