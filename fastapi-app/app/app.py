from fastapi import FastAPI, Request, Depends
from fastapi import HTTPException
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
        row = session.execute(select(Timestamp).where(Timestamp.id == t_id)).first()
        if not row:
            raise HTTPException(status_code=404, detail="Item not found")
        return {
            'id': row[0].id,
            'timestamp': row[0].timestamp,
        }
    

@app.post(
    path='/timestamp',
    tags=['Запись в БД'],
)
def post_timestamp(
    session = Depends(get_db),
):
    with session.begin():
        obj = Timestamp(timestamp=datetime.now())
        session.add(obj)
        session.flush()
        return obj.id
    
if __name__ == '__main__':
    uvicorn.run(
        'app:app',
        reload=True,
    )