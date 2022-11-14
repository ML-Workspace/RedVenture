from fastapi import FastAPI 
from pydantic import BaseModel
from typing import Optional

app= FastAPI()

taxonomies=[]

class Taxonomoy(BaseModel):
    tid: int
    tname: str
    vid: str
    is_parent: Optional[bool] = None

@app.get('/get/taxonomy')
def home():
    return taxonomies

@app.post('/add/taxonomy')
def add_taxonomy(data: Taxonomoy):
    taxonomies.append(data.dict())
    return {"message": taxonomies}
