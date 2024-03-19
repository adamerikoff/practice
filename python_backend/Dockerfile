FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

# Копируем и устанавливаем зависимости
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Копируем проект в контейнер
COPY . /app
