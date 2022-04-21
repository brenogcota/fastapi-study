
from typing import Optional
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    old: int
    is_active: Optional[bool] = True

users = []

@app.get("/")
def index():
    return RedirectResponse("/api/v1/users")

@app.get("/api/v1/users")
def all():
    return users

@app.post("/api/v1/users")
def create(user: User):
    users.append(user)
    return users

@app.get("/api/v1/users/{name}")
def one(name: str):
    return list(filter(lambda user: user.name == name, users))

@app.delete("/api/v1/users/{name}")
def delete(name: str):    
    to_remove = list(filter(lambda user: user.name != name, users))
    return to_remove
