# 11_dars_Type_Hints_va_Virtual_Environment

# 1. TYPE HINTS (Tur belgilash)
# Oddiy qilib: Funksiyaga "bu yerga matn keladi, bu yerdan son chiqadi" deb aytish
# Tasavvur qiling: siz bank xodimiga "bu qutiga faqat pul soling, poyabzal solmang" deb aytasiz. Type hints ham shunga o‘xshash.

# Typessiz (oddiy) — xato qilish oson:

# def qosh(a,b):
#     return a+b

# print(qosh(3,2)) #5(to'g'ri)
# print(qosh("5","2")) # 52 - bu xato matn kabi qo'shib qo'yadi 


# Type hints bilan (xato kam):
# def qosh(a: int,b: int) -> int :
#     return a+b

# print(qosh(3,2))
# print(qosh("3","2"))

# Tushuntirish:
# a: int — "a bu butun son"
# b: int — "b bu butun son"
# -> int — "bu funksiya butun son qaytaradi"


# FastAPI da juda ko‘p ishlatiladi:

# # FastAPI endpoint
# @app.get("/user/{user_id}")
# def get_user(user_id: int) -> dict:
#     return {"id": user_id, "name": "Ali"}

# # Pydantic modellari (ma'lumot tekshirish)
# class User(BaseModel):
#     name: str
#     age: int
#     email: str


# Turlar:
# def misol(
#     a: int,           # Butun son
#     b: float,         # O‘nlik son
#     c: str,           # Matn
#     d: bool,          # True/False
#     e: list,          # Ro‘yxat
#     f: dict,          # Lug‘at
#     g: list[int]      # Faqat sonlardan iborat ro‘yxat
# ) -> str:             # Matn qaytaradi
#     return "Salom"
# print(misol(11,1.1,"a",True,["Son"],{"ism" : "Ali"}, [1,2]))







# 2. VIRTUAL ENVIRONMENT (Virtual muhit)
# Oddiy qilib: Har bir loyiha uchun alohida "sumka"
# Tasavvur qiling:
# Loyiha 1 — Django 4.0 kerak
# Loyiha 2 — Django 3.0 kerak
# Agar hammasini bir joyga qo‘ysangiz, ular bir-biriga aralashadi. Virtual muhit — har bir loyiha uchun alohida sumka.

# Virtual environment yaratish:

# Yangi virtual muhit yaratish
# python -m venv myenv

# # Windows da ishga tushirish
# myenv\Scripts\activate

# # Mac/Linux da ishga tushirish
# source myenv/bin/activate

# # Deaktivatsiya
# deactivate

# Qayerda kerak?
# Turli loyihalar turli versiyalar kerak bo‘lganda
# Boshqa dasturchi sizning loyihangizni ishlatganda
# Serverga loyihani yuklaganda


# Barcha o‘rnatilgan kutubxonalarni faylga yozish
# pip freeze > requirements.txt


# # Fayl ichidagi hamma kutubxonalarni o‘rnatish
# pip install -r requirements.txt


# requirements.txt ko‘rinishi:
# fastapi==0.104.1
# uvicorn==0.24.0
# sqlalchemy==2.0.23




# ✅ Bugungi amaliy topshiriq
# 1-topshiriq (Type Hints):
# Quyidagi funksiyalarga type hints qo‘shing:

# def kopaytir(a : int, b : int)->int:
#     return a * b

# def salom_ber(ism : str, yosh : str)->str:
#     return f"{ism}, {yosh} yosh"

# def hisobla(sonlar:list)->float:
#     return sum(sonlar) / len(sonlar)

# print(kopaytir(2,3))
# print(salom_ber("Ali","20"))
# print(hisobla([1.2,22.0]))

# Natija:
# 6
# Ali, 20 yosh
# 11.6



