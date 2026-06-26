# 📘 5-DARS: POST — ma'lumot qo'shish (Create)
# Pydantic model (ma'lumot tekshirish):
# python
# from pydantic import BaseModel

# class UserCreate(BaseModel):
#     name: str
#     age: int
# POST endpoint:
# python
# @app.post("/users")
# def create_user(user: UserCreate):
#     db = SessionLocal()
#     db_user = User(name=user.name, age=user.age)
#     db.add(db_user)      # INSERT INTO ...
#     db.commit()          # Saqla
#     db.refresh(db_user)  # ID ni ol
#     db.close()
#     return db_user
