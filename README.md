# Тестовое задание на вакансию Django, TLT PRO
Решение тестового задания представляет собой проект Django
c настроенными моделями и админ-зоной. 
Модели описаны в директории

tlt_pro -> products -> models.py

## Как запустить проект
Клонировать репозиторий и перейти в него в командной строке:

```
git@github.com:VitaliiCheremisov/testing_task_tlt_pro.git
```

```
cd tlt_pro
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

* Если у вас Linux/macOS

    ```
    source env/bin/activate
    ```

* Если у вас windows

    ```
    source env/scripts/activate
    ```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
cd tlt_pro
python3 manage.py makemigrations
python3 manage.py migrate
```
Для запуска проекта локально c БД sqlite3:
1) В корневом каталоге создать .env файл
2) Описать переменные:
  * SECRET_KEY="'<ваш SECRET_KEY>'"

Например SECRET_KET="'django-insecure-k21i13@3f^h'"
  * ALLOWED_HOSTS="'<ваши ALLLOWED_HOSTS>'"'

Например ALLOWED_HOSTS="'localhost,web,127.0.0.1''"
```
cd tlt_pro
python3 manage.py runserver
```

Значения Суперюзера для проверки админ-зоны:
```
cd tlt_pro
python3 manage.py runserver createsuperuser
```
Указать данные, например:
- Электронная почта: admin@admin.com
- Username: admin_username
- Пароль: admin_password 
- Имя пользователя: admin

Технологии
```
Django 4.2
```

Автор
- [Виталий Черемисов](https://github.com/VitaliiCheremisov)
