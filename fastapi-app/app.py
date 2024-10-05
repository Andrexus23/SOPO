from fastapi import FastAPI, Request, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import select
from db import Session, Timestamp, Session
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
    t_id: int
):
    with Session as session, session.begin():
        return session.scalar(select(Timestamp).where(Timestamp.id == t_id)).first()
    

@app.post(
    path='/timestamp',
    tags=['Запись в БД'],
)
def post_timestamp(
    item: Item
):
    with Session as session, session.begin():
        obj = Timestamp(timestamp=item.timestamp)
        session.add(obj)
        session.flush()
        return obj.id
    
if __name__ == '__main__':
    uvicorn.run(
        'fastapi-app.app:app',
        reload=True,
    )