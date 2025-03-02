from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase


engine = create_async_engine("postgresql+asyncpg://ecommerce2:postgres@localhost:5432/ecommerce2", echo=True)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


class Base(DeclarativeBase):
    pass


"""
Подклчение к db sqlite
engine = create_engine('sqlite:///ecommerce.db', echo=True) 
SessionLocal = sessionmaker(bind=engine)
"""
