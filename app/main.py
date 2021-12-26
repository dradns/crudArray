from typing import Optional, List
from fastapi import FastAPI, Path
from pydantic import BaseModel

storage_arrays = \
{
    'id1': [4,5,2,7,9,0,1],
    'id2': [9,8,7,9,0,1],
    'id3': [9,6,4],
}

class Array12(BaseModel):
    myKey: List[int]

app = FastAPI()

@app.get("/array/{req_id}", response_model=Array12)
def return_array(req_id:str = Path(...,title = 'request identifier')):
    if req_id not in storage_arrays:
        return 'wrong id'
    return Array12(myKey=storage_arrays[req_id])

