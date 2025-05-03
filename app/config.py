from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL="mysql+mysqlconnector://root:1234@localhost:3306/biblioteca_db"


if not DATABASE_URL:
    raise ValueError("Error: La variable DATABASE_URL no está configurada correctamente")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()  # No pasar parámetros extra aquí
    try:
        yield db
    finally:
        db.close()