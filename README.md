<div align="center">

# FastAPI E-commerce

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/python-3.8+-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-red?style=for-the-badge&logo=sqlalchemy)](https://www.sqlalchemy.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

🛍️ Современный RESTful API для электронной коммерции на FastAPI

[Документация](#документация) •
[Установка](#установка) •
[Использование](#использование) •
[Разработка](#разработка)

</div>

## 📋 О проекте

FastAPI E-commerce - это высокопроизводительный API для электронной коммерции, построенный с использованием современного фреймворка FastAPI. Проект предоставляет полный набор функций для управления онлайн-магазином, включая работу с товарами, категориями и пользователями.

### 🚀 Ключевые возможности

- **Управление товарами**: CRUD-операции, поиск, фильтрация
- **Категории**: Иерархическая структура категорий
- **Аутентификация**: JWT-токены, OAuth2
- **Авторизация**: Ролевая система доступа
- **Документация**: Автоматическая OpenAPI (Swagger) документация
- **Безопасность**: Защита от CSRF, XSS, инъекций

## 🛠 Технологический стек

- **FastAPI**: Современный веб-фреймворк для создания API
- **SQLAlchemy**: Мощный ORM для работы с базой данных
- **Alembic**: Система миграций базы данных
- **Pydantic**: Валидация данных и сериализация
- **SQLite**: База данных (легко заменяется на PostgreSQL)
- **Python 3.8+**: Современный Python

## 📁 Структура проекта

```
app/
├── api/              # API endpoints
│   ├── v1/           # API версии 1
│   └── deps.py       # Зависимости
├── core/             # Ядро приложения
│   ├── config.py     # Конфигурация
│   └── security.py   # Безопасность
├── db/               # Работа с БД
│   └── session.py    # Сессии БД
├── models/           # Модели данных
├── schemas/          # Pydantic схемы
├── tests/            # Тесты
└── main.py          # Точка входа
```

## 🚀 Установка

1. **Клонирование репозитория**
```bash
git clone [URL репозитория]
cd fastapi_ecommerce
```

2. **Создание виртуального окружения**
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/MacOS
source venv/bin/activate
```

3. **Установка зависимостей**
```bash
pip install -r requirements.txt
```

4. **Настройка переменных окружения**
```bash
cp .env.example .env
# Отредактируйте .env файл
```

5. **Применение миграций**
```bash
alembic upgrade head
```

## 🎯 Использование

1. **Запуск сервера для разработки**
```bash
uvicorn app.main:app --reload
```

2. **Доступ к API**
- API: `http://localhost:8000`
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## 📝 API Endpoints

### Аутентификация
- `POST /auth/login` - Вход в систему
- `POST /auth/register` - Регистрация
- `POST /auth/refresh` - Обновление токена

### Товары
- `GET /products` - Список товаров
- `POST /products` - Создание товара
- `GET /products/{id}` - Детали товара
- `PUT /products/{id}` - Обновление товара
- `DELETE /products/{id}` - Удаление товара

### Категории
- `GET /categories` - Список категорий
- `POST /categories` - Создание категории

## 🔒 Безопасность

- Защита от CSRF-атак
- Валидация входных данных
- Rate limiting
- Безопасное хранение паролей

## 🧪 Тестирование

```bash
# Запуск тестов
python -m pytest

# С покрытием кода
python -m pytest --cov=app
```

## 📈 Мониторинг

Проект включает базовый мониторинг:
- Prometheus метрики
- Логирование в файл `logs/app.log`
- Трассировка запросов

## 📄 Лицензия

Распространяется под лицензией MIT. Смотрите [LICENSE](LICENSE) для деталей.

---

<div align="center">

**[⬆ Наверх](#fastapi-e-commerce)**

Сделано с ❤️ для сообщества FastAPI

</div>