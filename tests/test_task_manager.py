from task_manager import TaskManager


def test_task_manager_starts_empty():
    manager = TaskManager()
    assert manager.tasks == []

def test_add_task():
    manager = TaskManager()
    task = manager.add_task("Learn AI", "Practice AI")
    assert manager.tasks is not None
    assert task.title == "Learn AI"
    assert task.description == "Practice AI"

def test_find_task():
    manager = TaskManager()
    manager.add_task("Learn AI", "Practice AI")
    manager.add_task("Learn Python", "Practice Python")

    task1 = manager.find_task(2)
    task2 = manager.find_task(3)

    assert task1 is not None
    assert task2 is None

def test_complete_task():
    manager = TaskManager()
    task = manager.add_task("Learn AI", "Practice AI")
    manager.complete_task(task.id)

    assert task.completed == True

def test_edit_task():
    manager = TaskManager()
    task = manager.add_task("Learn AI", "Practice AI")
    manager.edit_task(task.id, "Learn Python", "Practice Python")

    assert task.title == "Learn Python"
    assert task.description =="Practice Python"

def test_delete_task():
    manager = TaskManager()
    task1 = manager.add_task("Learn AI", "Practice AI")
    task2 = manager.add_task("Learn Python", "Practice Python")
    manager.delete_task(task1.id)
    manager.delete_task(11)

    assert len(manager.tasks) == 1

def test_load_tasks(tmp_path):
    manager = TaskManager(tmp_path/"tasks.json")
    manager.add_task("Learn AI", "Practice AI")
    manager.add_task("Learn Python", "Practice Python")
    manager.add_task("Learn OOP", "Practice OOP")
    manager.save_tasks()

    manager.load_tasks()

    assert len(manager.tasks) ==3

    assert manager.tasks[0].title == "Learn AI"
    assert manager.tasks[1].title == "Learn Python"
    assert manager.tasks[2].title == "Learn OOP"

def test_save_tasks(tmp_path):
    manager = TaskManager(tmp_path / "tasks.json")
    manager.add_task("Learn about LLMs", "Check docs")
    manager.add_task("Learn about RAG", "Check docs")
    manager.save_tasks()

    manager.load_tasks()
    assert len(manager.tasks) == 2
    assert manager.tasks[0].title == "Learn about LLMs"
    assert manager.tasks[1].title == "Learn about RAG"


