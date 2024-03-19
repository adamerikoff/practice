# Проект: FastAPI приложение с PostgreSQL в Docker

## Обзор проекта
Этот проект представляет собой пример FastAPI приложения, использующего PostgreSQL в качестве базы данных. Приложение предоставляет API для управления предприятиями и их продуктами.

## Инструкции по сборке и запуску приложения с использованием Docker Compose

1. Установите Docker и Docker Compose на вашем компьютере, если они еще не установлены.

2. Склонируйте репозиторий на ваш компьютер:
    ```bash
    git clone https://github.com/your_username/your_project.git
    ```

3. Перейдите в директорию проекта:
    ```bash
    cd your_project
    ```

4. Создайте файл `.env` в корневой директории проекта и установите переменные окружения, необходимые для приложения и базы данных:
    ```plaintext
    # .env

    # Параметры приложения FastAPI
    APP_HOST=0.0.0.0
    APP_PORT=8000
    APP_DEBUG=True

    # Параметры PostgreSQL
    POSTGRES_DB=fastapi_db
    POSTGRES_USER=fastapi_user
    POSTGRES_PASSWORD=fastapi_password
    POSTGRES_HOST=db
    POSTGRES_PORT=5432
    ```

5. Запустите приложение с помощью Docker Compose:
    ```bash
    docker-compose up --build
    ```

6. После успешного запуска, приложение будет доступно по адресу [http://localhost:8000](http://localhost:8000).

7. Доступ к Swagger для API: [http://localhost:8000/docs](http://localhost:8000/docs).