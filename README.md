# completed-forms
Web-приложение для определения заполненных форм.

Стек: Django, TinyDB

# Запуск проекта без docker

### Подготовка виртуального окружения
```
python -m venv .venv
pip install pip install -r requirements.txt

```
### Запуск приложения
```
cd formmatcher
python manage.py migrate
python manage.py createsuperuser # при необходимости доступа к админки
python manage.py runserver
```

# Запуск проекта с docker
```
docker-compose up --build
```


# Дополнительно
Доступен post запрос 

```
/add_template для добавления новых форм
```
