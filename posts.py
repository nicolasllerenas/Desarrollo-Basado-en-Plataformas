from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
#Recuros
class Post(BaseModel):
    id:int
    likes:int
    comments:list[str]= None
    user:str
posts =[]
@app.get("/")
def hello():
    return "Hello, world from my API"
@app.get("/posts")
def get_posts():
    return posts
@app.get("/posts/{id}")
def get_post(post_id:int):
    for post in posts:
        if post.id==post_id:
            return post
@app.get("/posts")
def get_post_by_id(id:int):
    return None
@app.post("/posts")
def create_posts(post:Post):
    posts.append(post)
    return post