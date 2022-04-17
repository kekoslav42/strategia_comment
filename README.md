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
   [GET] api/v1/posts/
```
### Ответ
```bash
[
    {
        "id": 1,
        "comments": [],
        "author": "",
        "title": "",
        "text": "test",
        "published": "2022-04-17T09:09:23.847465Z"
    }
]
```
### Запрос
```bash
   [POST] api/v1/posts/
   {
    "author": "",
    "title": "",
    "text": "test"
    }
```
### Ответ
```bash
    HTTP 201 Created
```
### Запрос
```bash
   [GET] api/v1/comments/
```
### Ответ
```bash
[
    {
        "id": 1,
        "children": [],
        "title": "",
        "author": "",
        "published": "2022-04-17T10:10:32.658687Z",
        "level": 0,
        "parent": null,
        "post": 1
    }
]
```

### Запрос
```bash
   [POST] api/v1/comments/
   {
      {
    "title": "",
    "author": "",
    "parent": 1,
    "post": 1
      }
    }
```
### Ответ
```bash
    HTTP 201 Created
```

## Установка
