# 📘 2-DARS: Path va Query parametrlar
# Path parametr (yo'nalishdagi o'zgaruvchi):
# python
# @app.get("/user/{name}")
# def get_user(name: str):
#     return {"user": name}
# Misol: /user/Ali → {"user": "Ali"}

# Query parametr (? dan keyin):
# python
# @app.get("/users")
# def get_users(name: str = None, age: int = None):
#     # /users?name=Ali&age=20
#     return {"name": name, "age": age}
