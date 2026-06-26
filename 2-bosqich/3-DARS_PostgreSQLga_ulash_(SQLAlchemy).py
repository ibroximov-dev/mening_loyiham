# 📘 3-DARS: PostgreSQL ga ulash (SQLAlchemy)
# SQLAlchemy — "tarjimon":
# Siz Python da gapirasiz, u PostgreSQL ga tarjima qiladi.

# Ulanish:
# python
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:1234@localhost/fastapi_db"
# engine = create_engine(SQLALCHEMY_DATABASE_URL)
# SessionLocal = sessionmaker(bind=engine)
# Model (jadval ko'rinishi):
# python
# from sqlalchemy import Column, Integer, String
# from sqlalchemy.ext.declarative import declarative_base

# Base = declarative_base()

# class User(Base):
#     __tablename__ = "users"
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String)
#     age = Column(Integer)
