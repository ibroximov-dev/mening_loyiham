# 1. Sinxron — nima bu?
# Sinxron = Navbat (birma-bir)

# Tasavvur qiling: bitta kassa bor. Oldingi
# odam tugamaguncha, keyingi odamga navbat kelmaydi.

# import time

# def birinchi_mashina():
#     print("1-mashina yuvilmoqda...")
#     time.sleep(3)
#     print("1-mashina tayyor!")

# def ikkinchi_mashina():
#     print("2-mashina yuvilmoqda...")
#     time.sleep(3)
#     print("2-mashina tayyor!")


# birinchi_mashina()
# ikkinchi_mashina()


# 2. Asinxron — nima bu?
# Asinxron = Bir vaqtda (hammasi birdan)
# Tasavvur qiling: 3 ta kassa bor.
# Har bir mashina o'z kassasida birdan yuviladi.

# import asyncio

# async def mashina_yuv(nomi, vaqt):
#     print(f"{nomi} yuvilmoqda...")
#     await asyncio.sleep(vaqt)
#     print(f"{nomi} tayyor!")

# async def main():
#     await asyncio.gather(
#         mashina_yuv("1-mashina",3),
#         mashina_yuv("2-mashina",3),
#         mashina_yuv("3-mashina",3)
#     )

# asyncio.run(main())


# 5. Oddiy misol 
# — internetdan ma'lumot olish (tasavvur qiling)
# import asyncio

# async def malumot_ol(url,vaqt):
#     print(f"{url} dan ma'lumot olinmoqda...")
#     await asyncio.sleep(vaqt)
#     print(f"{url} malumot olindi!")
#     return f"Ma'lumot: {url}"

# async def main():
#     natijalar = await asyncio.gather(
#         malumot_ol("google.com",2),
#         malumot_ol("facebook.com", 1),
#         malumot_ol("instagram.com", 3)
#     )
#     print(f"Hamma malumotlar: {natijalar}")

# asyncio.run(main())



# uyga vazifa 

# import asyncio

# async def pishir(taom_nomi,vaqti ):
#     print (f"{taom_nomi} pishirmoqda... ({vaqti}) soniyada tayyor bo'ladi ")
#     await asyncio.sleep(vaqti)
#     print(f"{taom_nomi} tayyor! ")
#     return taom_nomi

# async def main():
#     natija = await asyncio.gather(
#         pishir("Manti", 5),
#         pishir("Sho'rva", 3),
#         pishir("Choy", 1)
#     )
#     print(f"Hamma taom tayyor: {natija}")
# asyncio.run(main())

# Qo'shimcha topshiriq
# 1
# import asyncio

# async def noushta(nomi,vaqt):
#     print(f"{nomi} tayyorlanmoqa ({vaqt}) soniyada tayyor bo'ladi!")
#     await asyncio.sleep(vaqt)  
#     return f"{nomi} tayyor!!!"


# async def  main():
#     natijalar = await asyncio.gather(
#         noushta("Qaymoq",2),
#         noushta("Asal",1),
#         noushta("Non",3),
#         noushta("Sariyog'",1)
#     )
#     print(f"Nunushta tayyor: {natijalar}")

# asyncio.run(main())




# 2
# import asyncio

# async def yuk_yetkaz(mashina, manzil, vaqt, keldi=""):
#     print(f"{mashina} ({manzil}) jo'nadi! ({vaqt} soniya)")
#     await asyncio.sleep(vaqt)
#     print(f"{mashina} ({manzil}) yetib keldi! {keldi} ")
#     return mashina

# async def main():
#     natijalar = await asyncio.gather(
#         yuk_yetkaz("1-mashina", "Buxoro", 4,"(oxri keldi)"),
#         yuk_yetkaz("2-mashina", "Samarqand", 2,"(birinchi)"),
#         yuk_yetkaz("3-mashina", "Toshkent", 3)
#     )

        
#     print(f"Hamma yuk yetkazildi! Umumiy vaqt: 4 soniya")
#     print(f"Ketma-ketlik: {natijalar}")
    

# asyncio.run(main())

# # 3
# import asyncio

# async def fayl_yukla():
#     print("Fayl yuklab olinmoqda...")
#     await asyncio.sleep(5)
#     print("Fayl yuklab olindi!")
#     return "fayl.jpg"
    

# async def db_sorov():
#     # Ma'lumotlar bazasiga so'rov (3 soniya)
#     print("Ma'lumotlar bazasiga so'rov yuborildi...")
#     await asyncio.sleep(3)
#     print(f"So'rov qabul qilindi!")
#     return "QABUL QILINDINGIZ!!!"

# async def email_yubor():
#     # Email yuborish (2 soniya)
#     print("Email yuborilmoqda...")
#     await asyncio.sleep(2)
#     print("Email tekshirildi!")
#     return "Xush kelibsiz: isroiljonibroximov2@gmail.com"


# async def main():
#     natijalar = await asyncio.gather(
#         fayl_yukla(),
#         db_sorov(),
#         email_yubor()
#     )
#     print(f"Natijalar: {natijalar}")
#     print(f"Eng tez jarayon: {natijalar[-1]}")
#     print(f"Eng sekin jarayon: {natijalar[0]}")
#     print(f"Umumiy vaqat 5 soniya!")

# asyncio.run(main())


# print("E'tiboringiz uchun katta raxmat😊")