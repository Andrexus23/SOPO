from fastapi import FastAPI, Request, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import select
from sqlalchemy.orm import Session
from db import Timestamp, get_db
from pydantic import BaseModel
from datetime import datetime
import uvicorn

app = FastAPI()

origins = [
    'http://localhost:8080',
    'http://127.0.0.1:8080',
    'http://127.0.0.1:5000',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

class Item(BaseModel):
    timestamp: datetime = datetime.now()

@app.get(
    path='/timestamp/{id}',
    tags=['Получить запись из БД'],
)
def get_timestamp(
    t_id: int,
    session = Depends(get_db),
):
    with session.begin():
        return session.scalar(select(Timestamp).where(Timestamp.id == t_id)).first()
    

@app.post(
    path='/timestamp',
    tags=['Запись в БД'],
)
def post_timestamp(
    item: Item,
    session = Depends(get_db),
):
    with session.begin():
        obj = Timestamp(timestamp=item.timestamp)
        session.add(obj)
        session.flush()
        return obj.id
    
if __name__ == '__main__':
    uvicorn.run(
        'app:app',
        reload=True,
    )