from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase



# Форма URL-адреса базы данных для PostgreSQL
# engine = create_engine('postgresql+psycopg2://youuser:youpassword@localhost/youdb') 


engine = create_engine('sqlite:///ecommerce.db', echo=True)
SessionLocal = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass