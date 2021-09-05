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
