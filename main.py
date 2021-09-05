from fastapi import FastAPI
from pydantic import BaseModel
from json_db import jsonDB


app = FastAPI()

db = jsonDB()


class Task(BaseModel):
    task_day: str
    start_time: str
    end_time: str
    name: str
    description: str


@app.get("/")
def root():
    return {"message": "sucess"}


@app.get("/tasks")
def get_tasks():
    data = db.get_all(table_name="tasks")

    return data


@app.get("/best_strategy")
def get_best_strategy():
    all_tasks = db.get_all(table_name="tasks")

    days = []
    for task in all_tasks:
        days.append(task["task_day"])

    days.sort(reverse=True)
    days = set(days)

    sorted_tasks = {}

    for day in days:
        sorted_tasks[day] = []
        for task in all_tasks:
            if task["task_day"] == day:
                sorted_tasks[day].append(task)
        sorted_tasks[day].sort(key=lambda x: x["end_time"])

    strategy = {}

    for day in sorted_tasks:
        tasks = sorted_tasks[day]
        strategy[day] = []
        strategy[day].append(tasks[0])
        del tasks[0]

        for task in tasks:
            if task["start_time"] >= strategy[day][-1]["end_time"]:
                strategy[day].append(task)

    return strategy


@app.post("/task")
def add_task(task: Task):

    db.add_item(table_name="tasks", item=task.dict())

    return task.dict()
