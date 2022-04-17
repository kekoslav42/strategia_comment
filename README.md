# strategia_comment

# Описание

API с возможностью добавления статей в базу данных и прикрипления к ним комментариев любого уровня вложенности.

#Доступные ссылки

```bash
api/v1/posts/ # Получение информации о всех постах
api/v1/posts/(?P<pk>[^/.]+)/ # Получение информации о выбранном посте
api/v1/comments/ # Получение информации о всех комментариях
api/v1/comments/(?P<pk>[^/.]+)/ # Получение информации о выбранном комментарии
```

# Примеры

### Запрос
```bash
   [GET] 127.0.0.1/api/v1/posts/
```
### Ответ
```bash
    {
        "id": 1,
        "comments": [],
        "author": "Anonymous",
        "title": "Not title",
        "text": "test",
        "published": "2022-04-17T14:00:47.492783Z"
    }
```
### Запрос
```bash
   [POST] 127.0.0.1/api/v1/posts/
   {
    "text": "test"
    }
```
### Ответ
```bash
    HTTP 201 Created
    {
    "id": 1,
    "comments": [],
    "author": "Anonymous",
    "title": "Not title",
    "text": "test",
    "published": "2022-04-17T14:00:47.492783Z"
    } 
```
### Запрос
```bash
   [GET] 127.0.0.1/api/v1/comments/
```
### Ответ
```bash
    {
        "id": 1,
        "children": [],
        "title": "Not title",
        "author": "Anonymous",
        "published": "2022-04-17T14:02:35.335060Z",
        "level": 0,
        "parent": null,
        "post": 1
    }
```

### Запрос

#### Если не указывается в запросе "parent": pk то комментарий создается без родителя
```bash
   [POST] 127.0.0.1/api/v1/comments/
   {
     "post": 1
   }
```
### Ответ
```bash
    HTTP 201 Created
    {
    "id": 1,
    "children": [],
    "title": "Not title",
    "author": "Anonymous",
    "published": "2022-04-17T14:02:35.335060Z",
    "level": 0,
    "parent": null,
    "post": 1
    }
```

## Установка
1. Установка docker и docker-compose

Инструкция по установке доступна в официальной инструкции

2. Создать файл .env с переменными окружения в папке infra

```bash
SECRET_KEY = Секретный ключ django

DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER= Пользователь базы данных
POSTGRES_PASSWORD= Пароль базы данных
DB_HOST= Хост базы данных
DB_PORT= Порт базы данных
```

3. Сборка и запуск контейнера(Выполняется в папке infra)

```bash
docker-compose up -d --build
```

4. Сбор статики

```bash
docker-compose exec web python manage.py collectstatic --noinput
```
5. Применение миграций

```bash
docker-compose exec web python manage.py migrate
```
