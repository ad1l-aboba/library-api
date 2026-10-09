# API для библиотеки книг

REST API на FastAPI. Данные хранятся в памяти (список).

## Запуск
```
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn main:app --reload
```
Документация и тестирование: http://127.0.0.1:8000/docs

## Эндпоинты
| Метод | Путь | Описание |
|-------|------|----------|
| GET | /books | Список всех книг |
| GET | /books/{id} | Книга по ID |
| POST | /books | Добавить книгу |
| PUT | /books/{id} | Обновить книгу |
| DELETE | /books/{id} | Удалить книгу |
