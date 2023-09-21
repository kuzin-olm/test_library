## Stack

- python 3.10
- PostgreSQL 14.8

## Зависимости

1. Зависимости пакетов:

```bash
$ pip install -r requirements.txt
```

2. Заполнить информацию о используемой БД:
   - alembic.ini [63 строка] для механизма миграций

   ```
   sqlalchemy.url = postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_DB_NAME}
   
   пример
   sqlalchemy.url = postgresql://admin:admin@127.0.0.1:5432/library
   ```

   - и файл настроек settings.py
   
   ```
   PG_USER = ...
   PG_PASSWORD = ...
   PG_HOST = ...
   PG_PORT = ...
   PG_DB_NAME = ...
   ```

3. Проинициализировать БД

   - если нужна чистая БД, то просто применить миграции
   
   ```bash
   $ alembic upgrade head
   ```
   
   - если нужен дамп БД
   
   ```bash
   $ sudo -u postgres psql -d {PG_DB_NAME} < dump.sql
   ```

4. старт

```bash
$ python main.py
```