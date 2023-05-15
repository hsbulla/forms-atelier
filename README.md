# Форма заказа для ателье одежды 

## MARK-UP:

Для запуска верстки необходимо выполнить:

1. cd markup-container
2. open index.html
3. activate live server

## WEB-INTERFACE (C БД в которую уходят данные из формы заказа с помощью POST запроса):

Для запуска сервера необходимо выполнить:

1. cd web-container
2. cd backend-container
3. python3 -m venv venv
4. source venv/bin/activate (venv\Scripts\activate.bat)
5. pip install -r requirements.txt
6. cd forms
7. python3 manage.py runserver localhost:5500

Для входа в административную панель в url необходимо добавить /admin/ (логин: formsadmin, пароль: formsadmin)
Для остановки сервера необходимо использовать комбинацию клавиш: ^C

*Написан на языке Python с использованием фреймворка Django

## DESKTOP-INTERFACE (C синхронизированной БД в которую также уходят данные из формы заказа):

Для запуска приложения выполнить:

1. cd desktop-container
2. python3 -m venv venv
3. source venv/bin/activate (venv\Scripts\activate.bat)
4. pip install -r requirements.txt
5. cd app-forms
6. python3 app.py

Предусмотрено параллельное использование WEB-INTERFACE и DESKTOP-INTERFACE
Выход из приложения осуществляется стандартным способом (Нажатием на крестик)

*Написан на языке Python с использованием фреймворка Eel


## Автор:
[@hsbulla](https://github.com/hsbulla) – Backend developer
