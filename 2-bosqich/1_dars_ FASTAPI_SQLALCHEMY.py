# 📘 FastAPI — bu nima?
# FastAPI — Python da REST API yozish uchun eng zamonaviy framework.

# Nima uchun FastAPI?
# ⚡ Tez — Node.js va Go bilan teng

# 📝 Avtomatik hujjat (Swagger UI) — brauzerda API sinab ko‘rish mumkin

# 🔍 Type hints bilan ishlaydi (siz o‘rgandingiz!)

# 🚀 O‘rganish oson — Django ga qaraganda tezroq

# 1-dars: Birinchi FastAPI server
# 1. FastAPI ni o‘rnatish
# bash
# # Yangi virtual muhit yarating (muhim!)
# python -m venv fastapi_env

# # Windows da ishga tushirish
# fastapi_env\Scripts\activate

# # FastAPI va serverni o‘rnatish
# pip install fastapi uvicorn
# 2. Birinchi API — "Salom, dunyo!"
# main.py fayl yarating:

# python
# from fastapi import FastAPI

# # FastAPI ilovasi yaratish
# app = FastAPI()

# # Endpoint (yo'nalish) yaratish
# @app.get("/")
# def home():
#     return {"message": "Salom, dunyo!"}

# @app.get("/about")
# def about():
#     return {"message": "Bu mening birinchi FastAPI loyiham"}

# @app.get("/user/{name}")
# def get_user(name: str):
#     return {"user": name, "message": f"Salom, {name}!"}
# 3. Serverni ishga tushirish
# bash
# uvicorn main:app --reload
# Tushuntirish:

# main — fayl nomi (main.py)

# app — FastAPI ilovasi nomi (app = FastAPI())

# --reload — o‘zgarishlarni avtomatik qayta yuklaydi

# 4. API ni sinab ko‘rish
# Brauzerda oching:

# http://localhost:8000 → {"message": "Salom, dunyo!"}

# http://localhost:8000/about → {"message": "Bu mening birinchi FastAPI loyiham"}

# http://localhost:8000/user/Ali → {"user": "Ali", "message": "Salom, Ali!"}

# 5. Avtomatik hujjat (Swagger UI)
# Brauzerda oching:

# http://localhost:8000/docs — Swagger UI (interaktiv)

# http://localhost:8000/redoc — Redoc (statik)

# 📝 Bugungi amaliy topshiriq
# 1. FastAPI ni o‘rnating
# 2. Yuqoridagi 3 ta endpoint ni yozing
# 3. Quyidagi endpoint ni qo‘shing:
# python
# @app.get("/math/{a}/{b}")
# def math(a: int, b: int):
#     return {
#         "qoshish": a + b,
#         "ayirish": a - b,
#         "kopaytirish": a * b,
#         "bolish": a / b
#     }
# Sinab ko‘ring: http://localhost:8000/math/10/5

# Natija:

# json
# {
#     "qoshish": 15,
#     "ayirish": 5,
#     "kopaytirish": 50,
#     "bolish": 2.0
# }
# ⭐ Qo‘shimcha qiyinroq variant
# python
# @app.get("/users")
# def get_users(name: str = None, age: int = None):
#     # Agar name berilsa, shu ismdagi foydalanuvchini qaytaring
#     # Agar age berilsa, shu yoshdagi foydalanuvchini qaytaring
#     pass




# topshiriq javoni:


# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def home():
#     return {"message": "Salom dunyo!"}

# @app.get("/about")
# def about():
#     return {"message" : "Bu mening birinchi Fastapi loyiham!"}

# @app.get("/users")
# def get_users(name: str = None, age: int = None): # type: ignore
#     users_db = [
#             {"id": 1, "name": "Ali", "age": 20},
#     {"id": 2, "name": "Vali", "age": 25},
#     {"id": 3, "name": "Hasan", "age": 18},
#     {"id": 4, "name": "Lola", "age": 22},
#     {"id": 5, "name": "Anvar", "age": 30}
#     ]

#     result = users_db

#     if name:
#         result = [user for user in result if user["name"].lower() == name.lower()]
    
#     # Agar age berilgan bo'lsa, filtrlash
#     if age:
#         result = [user for user in result if user["age"] == age]
    
#     return result



# @app.get("/math/{a}/{b}")
# def math(a:int, b:int):
#     return{ 
#         "qoshish" : a + b, 
#         "ayrish" : a - b,
#         "kopaytirish" : a * b,
#         "bo'lish" : a / b
#     }