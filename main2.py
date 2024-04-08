from fastapi import FastAPI, Response
from pydantic import BaseModel
#from typing import Optional
app = FastAPI()
class Item(BaseModel):
    id: int
    name: str
    stock: bool = True
items = []
@app.get("/")
def hello():
    return "Hello World"
@app.post("/items")
def add_item(item: Item, response: Response):
    response.status_code=201
    return {"item":item}
@app.get("/items")
def items():
    return items