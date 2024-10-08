"""Базовый класс и метаданные."""
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import DateTime
from sqlalchemy import Integer, create_engine, Engine
from sqlalchemy.orm import Mapped, mapped_column, sessionmaker
from sqlalchemy_utils import create_database, database_exists

class Base(DeclarativeBase):
    """Базовый класс для наследования всеми моделями."""


metadata = Base.metadata


class Timestamp(Base):

    __tablename__ = 'Timestamp'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    timestamp: Mapped[int] = mapped_column(DateTime)

conn_str: str = 'mysql+pymysql://root:password@localhost:3306/loykonen_matveev'
# mysql+pymysql://root:password@localhost:5000/loykonen_matveev
# 'mysql+pymysql://root:password@mysql.loykonen-matveev.svc.cluster.local:3306/loykonen_matveev'
if not database_exists(conn_str):
    create_database(conn_str)

engine: Engine = create_engine(conn_str)
SessionGenerator = sessionmaker(engine)



metadata.create_all(bind=engine)

async def get_db():
    db = SessionGenerator()
    try:
        yield db
    finally:
        db.close()
