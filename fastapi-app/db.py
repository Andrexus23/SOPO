"""Базовый класс и метаданные."""
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import DateTime
from sqlalchemy import Integer, create_engine, Engine
from sqlalchemy.orm import Mapped, mapped_column, sessionmaker

class Base(DeclarativeBase):
    """Базовый класс для наследования всеми моделями."""


metadata = Base.metadata


class Timestamp(Base):

    __tablename__ = 'Timestamp'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    timestamp: Mapped[int] = mapped_column(DateTime)

engine: Engine = create_engine('')
Session = sessionmaker(engine)
