from app.backend.db import Base
from sqlalchemy import Column, Integer, String, Boolean


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)
    is_supplier = Column(Boolean, default=False)
    is_customer = Column(Boolean, default=True)



"""
    id - Поле первичного ключа модели.
    first_name - Поле имени пользователя.
    last_name - Поле фамилии пользователя.
    username - Поле логина пользователя.
    email - Поле E-Mail пользователя
    hashed_password - Поле хранения хэшированного пароля. Хранить не хэшированный пароль не безопасно, поэтому мы будем хранить только его хэш.
    is_active - Поле хранящее булево значение, значение False будет использоваться в случае удаления пользователя, чтобы заблокировать доступ к некоторым разделам API. По умолчанию используется значение True.
    is_admin - Поле хранящее булево значение, значение True будет использоваться только для администратора, чтобы предоставить доступ к некоторым разделам API. По умолчанию значение False.
    is_supplier - Поле хранящее булево значение, значение True будет использоваться только для продавцов товара, чтобы предоставить доступ к некоторым разделам API, например как добавление товара. По умолчанию значение False.
    is_customer - Поле хранящее булево значение, значение True будет использоваться только для покупателей товара. По умолчанию значение True.
"""