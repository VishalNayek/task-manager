from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from task_manager import TaskManager

class TaskCreate(BaseModel):
    title: str
    description: str

class TaskResponse(BaseModel):
    id: int
    title: str
    description: str
    completed: bool

class TaskMessageResponse(BaseModel):
    message: str
    task: TaskResponse



app = FastAPI()
manager = TaskManager()
manager.load_tasks()

@app.get("/")
def get_root():
    return {"message" : "Welcome to FASTAPI"}

@app.get("/tasks", response_model=list[TaskResponse])
def get_tasks():
    task_list = []
    for task in manager.tasks:
        task_list.append(task.to_dict())
    return task_list

@app.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task_by_id(task_id : int):
    task = manager.find_task(task_id)
    if task is not None:
        return task.to_dict()
    else:
        raise HTTPException(status_code=404, detail="Task not Found")

@app.post("/tasks", response_model=TaskMessageResponse, status_code=201)
def create_tasks(task : TaskCreate):
    new_task = manager.add_task(task.title, task.description)
    manager.save_tasks()
    return {
        "message" : "Task created Successfully",
        "task" : new_task.to_dict()
    }

@app.put("/tasks/{task_id}", response_model=TaskMessageResponse)
def edit_task(task_id : int, task : TaskCreate):
    task_by_id = manager.find_task(task_id)
    if task_by_id is not None:
        manager.edit_task(task_id, task.title, task.description)
        manager.save_tasks()
        return {
            "message": "Task updated successfully",
            "task": task_by_id.to_dict()
        }
    else:
        raise HTTPException(status_code=404, detail="Task not found")

@app.patch("/tasks/{task_id}/complete", response_model=TaskMessageResponse)
def complete_task(task_id : int):
    task = manager.find_task(task_id)
    if task is not None:
        manager.complete_task(task_id)
        manager.save_tasks()
        return {
            "message": "Task completed successfully",
            "task": task.to_dict()
        }
    else:
        raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{task_id}")
def delete_task(task_id:int):
    task_by_id = manager.find_task(task_id)
    if task_by_id is not None:
        manager.delete_task(task_id)
        manager.save_tasks()
        return {"message" : "Task Deleted Successfully!"}
    else:
        raise HTTPException(status_code=404, detail="Task not found")