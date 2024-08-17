# Тестовое задание на вакансию Django, TLT PRO
Решение тестового задания представляет собой проект Django
c настроенными моделями и админ-зоной, модели описаны в директории
tlt_pro -> products -> models.py

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

- Электронная почта: admin@admin.com
- Username: admin_username
- Пароль: admin_password 
- Имя пользователя: admin 
- Фамилия: admin

Технологии
```
Django 4.2
```

Автор
- [Виталий Черемисов](https://github.com/VitaliiCheremisov)
