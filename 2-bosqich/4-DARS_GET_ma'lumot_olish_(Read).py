# 📘 4-DARS: GET — ma'lumot olish (Read)
# Hamma foydalanuvchilarni olish:
# python
# @app.get("/users")
# def get_users():
#     db = SessionLocal()
#     users = db.query(User).all()  # SELECT * FROM users
#     db.close()
#     return users
# Bitta foydalanuvchini ID bo'yicha olish:
# python
# @app.get("/users/{user_id}")
# def get_user(user_id: int):
#     db = SessionLocal()
#     user = db.query(User).filter(User.id == user_id).first()
#     db.close()
#     if not user:
#         return {"error": "Foydalanuvchi topilmadi"}
#     return user
