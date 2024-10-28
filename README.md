**Пет-проект по бронированию номеров отелей**
___

Здесь вы можете ознакомиться с моим приложением по бронированию номеров отелей. Приложение написано на языке Pyhton на платформе FastAPI. Также при создании данного приложения и работе с ним мы использовали такие инструменты программирования как SQL, SQLAlchemy, Redis, Celery, Flower и др.

Описание работы с проектом:
•	Составлял пет-проект на языке Python3.12
•	Работу с проектом осуществлял на фреймворке FastAPI через Swagger
•	Писал SQL запросы к PostgreSQL
•	Применял асинхронность (asyncio) для улучшения производительности работы кода
•	Использовал кэширование Redis
•	Осуществлял подключение Celery для оправки сообщения на почту пользователя
•	Запускал Flower
•	Работал с SQLAdmin
•	Создавал и дополнял свой проект в удаленный репозиторий на Github
•	Реализовал контейнеризацию проекта через Docker
•	Осуществлял развертывание проекта в облаке
•	Работал с Nginx
___

**Запуск приложения**

Для запуска FastAPI используется веб-сервер uvicorn. Команда для запуска выглядит так:
```uvicorn app.main:app --reload```
Ее необходимо запускать в командной строке, обязательно находясь в корневой директории проекта.
___
**Celery & Flower**

Для запуска Celery используется команда:
```celery --app=app.tasks.celery:celery worker -l INFO -P solo```
Обратите внимание, что -P solo используется только на Windows, так как у Celery есть проблемы с работой на Windows.
Для запуска Flower используется команда:
```celery --app=app.tasks.celery:celery flower```
___
**Dockerfile**
Для запуска веб-сервера (FastAPI) внутри контейнера необходимо раскомментировать код внутри Dockerfile и иметь уже запущенный экземпляр PostgreSQL на компьютере. Код для запуска Dockerfile:
```docker build .```
Команда также запускается из корневой директории, в которой лежит файл Dockerfile.
___
**Docker compose**

Для запуска всех сервисов (БД, Redis, FastAPI, Celery, Flower) необходимо использовать файл docker-compose.yml и команды
```docker compose build```
```docker compose up```
