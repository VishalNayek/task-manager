from task import Task

def test_create_task():
    task = Task(1, "Learn Python", "Learn pytest")

    assert task.title == "Learn Python"
    assert task.description == "Learn pytest"
    assert task.completed == False

def test_complete_task():
     task = Task(1, "Learn Python", "Learn pytest")
     task.complete()
     assert task.completed == True

def test_edit_task():
      task = Task(1, "Learn Python", "Learn pytest")
      task.edit("Learn AI", "Learn LLM")
      assert task.title == "Learn AI"
      assert task.description == "Learn LLM"

def test_to_dict():
    task = Task(1, "Learn Python", "Learn pytest")
    result = task.to_dict()

    assert result == {
        "id": 1,
        "title": "Learn Python",
        "description": "Learn pytest",
        "completed": False
    }

def test_from_dict():
    data = {
        "id": 1,
        "title": "Learn Python",
        "description": "Learn pytest",
        "completed": True
    }
    task = Task.from_dict(data)

    assert isinstance(task, Task)

    assert task.id == 1
    assert task.title =="Learn Python"
    assert task.description == "Learn pytest"
    assert task.completed == True