#!/usr/bin/env python

# https://fastapi.tiangolo.com/tutorial/first-steps/

from fastapi import FastAPI
from fastapi.params  import Body
from pydantic import BaseModel

app = FastAPI()



class Post(BaseModel):
   title: str
   content: str


@app.get("/")
def root():
   return {"message": "Welcome to my API!"}

# #Path Parameters
@app.get("/posts")
def get_posts():
   return {"data": "This is your posts"}

#Path Parameters with types
@app.post("/createposts")
def create_posts(new_posts:Post): # FAST API will reference the class we created earlier and it will check if it has a title or content and make sure they are strings if 
   # Python will throw an error
   print(payload)
   return {"new_post": f"title {payload['title']} content: {payload['content']}"}

# title str, content str
    