from typing import List

from fastapi import FastAPI, Body, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from database.connection import get_db
from database.orm import ToDo
from database.repository import get_todos

app =FastAPI()
todo_data = {}
@app.get("/")
def health_check_handler():
    return {"ping": "pong"}

@app.get("/todos")
def get_todos_handler(
    order: str = None,
    session: Session = Depends(get_db),
):
    todos: List[ToDo] = get_todos(session= session)

    if order == "DESC":
        return todos[::-1]
    return todos

@app.get("/todos/{todo_id}", status_code=200)
def get_todos_handler(todo_id: int):
    ret = todo_data.get(todo_id)
    if ret:
        return ret
    raise HTTPException(status_code=404, detail="ToDo Not Found")

class CreateToDoRequest(BaseModel):
    id: int
    contents: str
    is_done: bool

#  todo 생성
@app.post("/todos", status_code=201)
def create_todos_handler(request: CreateToDoRequest):
    todo_data[request.id] = request.dict()
    return todo_data[request.id]

# 아이디를 검색하여 is_done 수정여부
@app.patch("/todos/{todo_id}", status_code=201)
def update_todo_handler(
        todo_id: int,
        is_done: bool = Body(..., embed=True),
):
    todo = todo_data.get(todo_id)

    if todo:
        todo["is_done"] = is_done
        return todo
    raise HTTPException(status_code=404, detail="ToDo Not Found")


@app.delete("/todos/{todo_id}",status_code=204)
def delete_todo_handler(todo_id: int):
    res = todo_data.pop(todo_id, None)
    if res:
        return
    raise HTTPException(status_code=404, detail="ToDo Not Found")