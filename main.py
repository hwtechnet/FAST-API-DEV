#!/usr/bin/env python

from fastapi import Body, FastAPI

app = FastAPI()

@app.get("/")
async def root():
   return {"message": "Hello World"}

# #Path Parameters


#Path Parameters with types

    