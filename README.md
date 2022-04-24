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

```bash
api/v2/posts/ # Получение информации о всех постах
api/v2/posts/(?P<pk>[^/.]+)/ # Получение информации о выбранном посте
api/v2/comments/ # Получение информации о всех комментариях
api/v2/comments/(?P<pk>[^/.]+)/ # Получение информации о комментариях к посту
```

# Документация

### Описана на swagger находится в папке docs в файле docs.yml
```bash
https://app.swaggerhub.com/apis/kekoslav42/comment_api/2
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
