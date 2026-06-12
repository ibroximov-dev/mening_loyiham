# 5-dars {dict{kalit : qiymat}}

# 1. Lug‘at yaratish
# talaba = {
#     "ism" : "Ali",
#     "yosh" : 20,
#     "kurs" : 3,
#     "darslar" : ["Python", "SQL", "Django"]
# }

# print(talaba)



# 2. Qiymatga murojaat qilish
# talaba = {
#     "ism" : "Ali",
#     "yosh" : 20,
#     "kurs" : 3
# }

# print(talaba["ism"]) 
# print(talaba["yosh"]) 
# # Xavfsiz usul (agar kalit bo'lmasa xato bermaydi)
# print(talaba.get("mol"))
# print(talaba.get("mol","Topilmadi"))


# # 3. Lug‘atga ma'lumot qo‘shish va o‘zgartirish
# talaba = {"ism": "Ali"}

# # Qo‘shish
# talaba["yosh"] = 20 # type: ignore
# talaba["kurs"] = 4 # type: ignore
# print(talaba)

# # O'zgartirish
# talaba["yosh"] = 21 # type: ignore
# print(talaba)


# 4. Lug‘atdan ma'lumot o‘chirish
# talaba = {"talaba" : "Ali", "yosh" : 20, "kurs" : 3}

# # Kalit bo'yicha o'chirish
# del talaba["kurs"]
# print(talaba)

# # pop() — o‘chiradi va qiymatini qaytaradi
# yosh = talaba.pop("yosh")
# print(yosh)
# print(talaba)

# # Hammasini tozalash
# talaba.clear()
# print(talaba)


# 5. Lug‘at bo‘ylab aylanish (for)
# talaba = {
#     "ism" : "Ali",
#     "yosh" : 20,
#     "kasb" : "dasturchi"
# }

# # Kalit bo'ylab  
# for kalit in talaba:
#     print(f"{kalit}: {talaba[kalit]}")

# # kalit va qiymat bo'ylab 
# for kalit, qiymat in talaba.items():
#     print(f"{kalit} -> {qiymat}")


# # Faqat kalit bo'ylab
# for kalit in talaba.keys():
#     print(kalit)
# # Faqat qiymat bo'ylab
# for qiymat in talaba.values():
#     print(qiymat)

# 6. Ro‘yxat ichida lug‘at (juda muhim!)
# Backend dasturlashda JSON ma'lumotlar ko‘pincha shunday keladi:
# talabalar = [
#     {"ism": "Ali", "yosh": 20, "kurs": 3},
#     {"ism": "Vali", "yosh": 21, "kurs": 4},
#     {"ism": "Hasan", "yosh": 19, "kurs": 2}
# ]

# Har bir talabani chiqarish
# for talaba in talabalar:
#     print(f"{talaba['ism']} - {talaba['yosh']}-yosh {talaba['kurs']}-kurs")

# uyga vazifa

# talabalar = [
#     {"ism" : input("1-odamning ismi: "), "yosh" : int(input("1-odamning yoshi: ")), "manzli" : input("1-odamning manzili: ")},
#     {"ism" : input("2-odamning ismi: "), "yosh" : int(input("2-odamning yoshi: ")), "manzli" : input("2-odamning manzili: ")},
#     {"ism" : input("3-odamning ismi: "), "yosh" : int(input("3-odamning yoshi: ")), "manzli" : input("3-odamning manzili: ")}
# ]
# print(f'Barcha Odamlar:')
# for talaba in talabalar:
#     print(f" {talaba['ism']} - {talaba['yosh']}, {talaba['manzli']}")

# print("Yoshi 18 dan katta odamlar:")
# for cheklov in talabalar: 
#     if cheklov["yosh"] >= 18:
#         print(f"{cheklov['ism']} - {cheklov['yosh']}, {cheklov['manzli']}")











