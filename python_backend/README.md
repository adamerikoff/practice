# Проект: FastAPI приложение с PostgreSQL в Docker

## Обзор проекта
Этот проект представляет собой пример FastAPI приложения, использующего PostgreSQL в качестве базы данных. Приложение предоставляет API для управления предприятиями и их продуктами.

## Инструкции по сборке и запуску приложения с использованием Docker Compose

1. Установите Docker и Docker Compose на вашем компьютере, если они еще не установлены.

2. Склонируйте репозиторий на ваш компьютер:
    ```bash
    git clone https://github.com/adamerikoff/practice.git
    ```

3. Перейдите в директорию проекта:
    ```bash
    cd python_backend
    ```

5. Запустите приложение с помощью Docker Compose:
    ```bash
    docker-compose up --build
    ```

6. После успешного запуска, приложение будет доступно по адресу [http://localhost:8000](http://localhost:8000).

7. Доступ к Swagger для API: [http://localhost:8000/docs](http://localhost:8000/docs).