# 📘 10-dars: Decorator va Generator

# Oddiy qilib: Funksiyaga qo'shimcha funksiya qo'shish
# Tasavvur qiling: sizda choy bor. Decorator — bu choyga shakar yoki limon qo'shishga o'xshaydi. Asosiy funksiya o'zgarmaydi, lekin unga yangi xususiyat qo'shiladi.

# Oddiy funksiya:
# def salom_ber():
#     print("Salom")

# salom_ber()  #Salom

# Decorator bilan — choyga shakar qo'shish:
# def shakar_qosh(func):
#     def ichki():
#         print("Shakar qo'shildi!")
#         func()
#         print("Choy tayyor!")
#     return ichki

# @shakar_qosh
# def choy_tayyorla():
#     print("Choy damladim!")

# choy_tayyorla()

# Natija:  
# 🍬 Shakar qo'shildi
# Choy damlandi
# 🍵 Choy tayyor!

# E'tibor bering: choy_tayyorla() funksiyasining o'ziga hech narsa qo'shmadik, lekin u endi shakar bilan keldi!



# Real hayotdagi misol (backendda):
# Bu decorator faqat adminlar uchun ruxsat tekshiradi
# def admin_kerek(func):
#     def ichki(foydalanuvchi):
#         if foydalanuvchi != "admin":
#             print("Qabul qilinmadi!")
#             return
#         return func(foydalanuvchi)
#     return ichki

# @admin_kerek
# def panel(foydalanuvchi):
#     print(f"Xush kelibsiz: {foydalanuvchi}")

# panel("admin") #Xush kelibsiz: admin
# panel("Ali") #Qabul qilinmadi!


# Qayerda ishlatiladi?
# FastAPI/Django da login tekshirish
# Vaqtni hisoblash (funksiya qancha vaqt ishladi)
# Log yozish (funksiya ishga tushganini yozib qo'yish)

# Vaqtni hisoblovchi decorator:
# import time 

# def vaqtni_ol(func):
#     def ichki():
#         boshlanishi = time.time()
#         func()
#         tugash = time.time()
#         print(f"Vaqt: {tugash - boshlanishi} soniya")
#     return ichki

# @vaqtni_ol
# def uxla():
#     time.sleep(2)
#     print("uxlab turdim...")

# uxla()  #uxlab turdim...
# Vaqt: 2.0008139610290527 soniya





# 2. GENERATOR (Yaratuvchi)
# Oddiy qilib: Bir martada hamma ma'lumotni emas, kerakligicha beruvchi
# Tasavvur qiling: sizda 1000 ta kitob bor. Hammasini birdan olib kelish o'rniga, har safar bittasini olib kelasiz. Bu xotirani tejaydi.

# Oddiy funksiya (ro'yxat qaytaradi):
# def sonlar_royxati(n):
#     royxat = []
#     for i in range(n+1):
#         royxat.append(i)
#     return royxat
# for son in sonlar_royxati(5):
#     print(son)

# Bu yerda hamma sonlar birdan xotiraga joylanadi.


# Generator (yield bilan):
# def sonlar_generatori(n):
#     for i in range(n+1):
#         yield i  # yield — "hozircha shuni ber, keyin davom et"
    
# for son in sonlar_generatori(5):
#     print(son)  # 0,1,2,3,4,5 (lekin xotiraga hammasi joylanmaydi)
# Farqi: yield funksiyani to'xtatib, qiymat qaytaradi va keyingi chaqiruvda davom ettiradi.


# Real hayotdagi misol:
# Katta faylni o'qish (masalan, 10 GB)
# def katta_fayl_oych(fayl_nomi):
#     with open(fayl_nomi, 'r') as fayl:
#         for qator in fayl:
#             yield qator  # Bir qatorni ber, keyin to'xta

# # Ishlatish
# for qator in katta_fayl_oych("katta_fayl.txt"):
#     print(qator)  # 10 GB faylni ham xotiraga sig'dira oladi


# Qayerda ishlatiladi?
# Katta ma'lumotlarni o'qish (API dan sahifalab ma'lumot olish)
# Cheksiz ketma-ketliklar (masalan, Fibonachchi sonlari)
# Database dan ko'p ma'lumot olish
# Cheksiz generator misol:

# def cheksiz_son():
#     son = 0
#     while True:
#         yield son
#         son += 1

# for son in cheksiz_son():
#     print(son)
#     if son > 10:
#         break  # Cheksizni to'xtatish kerak


# Tasavvur qiling: sizda 1000 ta konfet bor.
# Oddiy ro'yxat: hamma 1000 ta konfetni birdan stolga tashlaysiz (xotira to'lib ketishi mumkin)
# Generator: har safar 1 ta konfet beradi, keyin "yana kerak bo'lsa, yana beraman" deydi
# 1. Oddiy funksiya (ro'yxat qaytaradi)
# def konfet_bor():
#     return [1,2,3,4,5]  # Hammasini birdan beradi

# hammasi = konfet_bor()
# print(hammasi)  #[1, 2, 3, 4, 5]


# 2. Generator (yield bilan)
# def konfet_bor():
#     yield 1
#     yield 2
#     yield 3
#     yield 4
#     yield 5

# konfet = konfet_bor()
# print(next(konfet)) #1
# print(next(konfet)) #2
# print(next(konfet)) #3
# Farqi: Har safar next() chaqirilganda, keyingi qiymat keladi. Hammasini birdan xotiraga joylamaydi


# 3. For siklida ishlatish (eng ko'p ishlatiladigan usul)
# def konfet_bor():
#     for i in range(6):
#         yield i 

# for konfet in konfet_bor():
#     print(konfet)


# 4. Juft sonlar generatori (sizning topshirig'ingiz)
# def juft_sonlar():
#     son = 2
#     while True:           # Cheksiz davom etadi
#         yield son         # Hozirgi sonni ber
#         son += 2          # Keyingi juft songa o't

# # Ishlatish
# for son in juft_sonlar():
#     if son > 20:          # 20 dan katta bo'lsa to'xta
#         break
#     print(son)            # 2,4,6,8,10,12,14,16,18,20


# 5. Generator nimaga foydali?
# Ro'yxat (List)	Generator
# Hammasini birdan xotiraga joylaydi	Bir vaqtda bitta qiymat saqlaydi
# 1 million son → 8 MB xotira	1 million son → bir necha bayt
# Xotira yetmasligi mumkin	Xotira muammosi bo'lmaydi



# 📊 Decorator vs Generator:
# Decorator	   ---     Generator
# Funksiyaga qo'shimcha qo'shadi	----  Qiymatlarni kerakligicha beradi
# @ bilan ishlatiladi	----------  yield bilan ishlatiladi
# Login tekshirish, vaqt hisoblash  --------------- 	Katta ma'lumotlar, cheksiz ketma-ketlik



# ✅ Bugungi amaliy topshiriq:
# # 1-topshiriq (Decorator):

# def decorator(func):
#     def ichki(ism):
#         print("Jarayon boshlandi...")
#         func(ism)
#         print("Jarayon tugadi!!")
#     return ichki

# @decorator
# def salom_ber(ism):
#     print(f"Salom {ism}")


# salom_ber(input("Ismingizni kiriting: "))



# 2-topshiriq

# def juft_sonlar():
#     son = 2 
#     while True:
#         yield son
#         son += 2 

# # 20 gacha chiqarish
# for son in juft_sonlar():
#     if son > 20:
#         break
#     print(son)
