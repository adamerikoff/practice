from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL для подключения к базе данных PostgreSQL
SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:postgres@localhost:5432/reviro"

# Создаем объект engine для взаимодействия с базой данных
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Создаем объект sessionmaker для создания сессий базы данных
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Создаем базовый класс для определения моделей данных
Base = declarative_base()

# Функция для получения сессии базы данных
def get_db():
    # Создаем сессию базы данных
    db = SessionLocal()
    try:
        # Возвращаем сессию в качестве генератора
        yield db
    finally:
        # После завершения использования сессии закрываем ее
        db.close()
