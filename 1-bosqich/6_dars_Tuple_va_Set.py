# # 📘 6-dars: Tuple va Set

# 1. TUPLE (o'zgarmas ro'yxat)
# Tuple — ro‘yxatga o‘xshaydi, lekin o‘zgarmaydi (yaratgandan keyin o‘zgartirib bo‘lmaydi).

# Yaratish:
# python
# # Ro‘yxat (o‘zgaruvchan)
# royxat = [1, 2, 3]

# # Tuple (o‘zgarmas)
# tuple_1 = (1, 2, 3)
# tuple_2 = 4, 5, 6  # Qavssiz ham bo'ladi
# bitta_element = (5,)  # Bitta elementli tuple (vergul kerak!)
# Asosiy farqlar:
# python
# # Ro‘yxat — o‘zgartirish mumkin
# royxat = [1, 2, 3]
# royxat[0] = 10  # ✅ Ishlaydi
# royxat.append(4)  # ✅ Ishlaydi

# # Tuple — o‘zgartirish mumkin EMAS
# tuple_1 = (1, 2, 3)
# tuple_1[0] = 10  # ❌ XATO! TypeError
# tuple_1.append(4)  # ❌ XATO!
# Qiymat olish (ro‘yxat bilan bir xil):
# python
# tuple_1 = (10, 20, 30, 40, 50)

# print(tuple_1[0])     # 10
# print(tuple_1[1:4])   # (20, 30, 40)
# print(len(tuple_1))   # 5

# for son in tuple_1:
#     print(son)
# Tuple qayerda ishlatiladi?
# python
# # API dan kelgan o'zgarmas ma'lumotlar
# hafta_kunlari = ("Dushanba", "Seshanba", "Chorshanba", "Payshanba", "Juma", "Shanba", "Yakshanba")

# # Koordinatalar (x, y)
# nuqta = (10, 20)

# # Funksiyadan bir nechta qiymat qaytarish
# def sonlarni_ayir_va_qosh(a, b):
#     return (a + b, a - b)  # Tuple qaytaradi
# 2. SET (takrorlanmaydigan to'plam)
# Set — takrorlanmaydigan elementlar to'plami. Ro'yxatga o'xshaydi, lekin indeks YO'Q!

# Yaratish:
# python
# # Set yaratish
# set_1 = {1, 2, 3, 4, 5}

# # Bo'sh set (diqqat! {} lug'at, set emas)
# bo_sh_set = set()  # To'g'ri
# # bo_sh_set = {}  # ❌ Bu lug'at, set emas!

# # Ro'yxatdan set yaratish (takrorlarni yo'qotish)
# royxat = [1, 2, 2, 3, 3, 3, 4]
# set_2 = set(royxat)
# print(set_2)  # {1, 2, 3, 4} — takrorlanuvchilar yo'q
# Set xususiyatlari:
# python
# # 1. Takrorlanmaydi
# set_1 = {1, 2, 2, 3, 3, 3}  # {1, 2, 3}

# # 2. Indeks YO'Q (murojaat qilib bo'lmaydi)
# set_1 = {10, 20, 30}
# # print(set_1[0])  # ❌ XATO! TypeError

# # 3. Tartib SAQLANMAYDI (har safar boshqacha chiqishi mumkin)
# Set bilan amallar:
# python
# set_1 = {1, 2, 3, 4, 5}
# set_2 = {4, 5, 6, 7, 8}

# # Qo'shish
# set_1.add(6)  # {1, 2, 3, 4, 5, 6}

# # O'chirish
# set_1.remove(3)  # {1, 2, 4, 5, 6}

# # Bir nechta qo'shish
# set_1.update([7, 8, 9])  # {1, 2, 4, 5, 6, 7, 8, 9}

# # Birlashma (union)
# birlashma = set_1 | set_2  # yoki set_1.union(set_2)

# # Kesishma (intersection)
# kesishma = set_1 & set_2  # yoki set_1.intersection(set_2)

# # Farq (difference)
# farq = set_1 - set_2  # set_1 da bor, lekin set_2 da yo'q

# print(f"Birlashma: {birlashma}")
# print(f"Kesishma: {kesishma}")
# Set bo'ylab aylanish:
# python
# set_1 = {10, 20, 30, 40, 50}

# for son in set_1:
#     print(son)  # Tartibsiz chiqadi (10, 50, 20, 40, 30...)
# Set qayerda ishlatiladi?
# python
# # 1. Takrorlanuvchilarni yo'qotish
# foydalanuvchilar = ["Ali", "Vali", "Ali", "Hasan", "Vali"]
# unikallar = set(foydalanuvchilar)
# print(unikallar)  # {'Ali', 'Vali', 'Hasan'}

# # 2. Ikkala ro'yxatda ham bor elementlarni topish
# adminlar = {"Ali", "Hasan"}
# foydalanuvchilar = {"Ali", "Vali", "Hasan", "Olim"}
# huquqli = adminlar & foydalanuvchilar  # {'Ali', 'Hasan'}

# # 3. Tez qidiruv (set da qidirish ro'yxatga qaraganda tezroq)
# 3. Uchchalasining taqqoslanishi:
# Xususiyat	List (Ro'yxat)	Tuple	Set
# O'zgaruvchan	✅ Ha	❌ Yo'q	✅ Ha
# Indeks bor	✅ Ha	✅ Ha	❌ Yo'q
# Takrorlanish mumkin	✅ Ha	✅ Ha	❌ Yo'q
# Tartib saqlaydi	✅ Ha	✅ Ha	❌ Yo'q
# Qachon ishlatiladi	Dinamik ma'lumotlar	O'zgarmas ma'lumotlar	Unikal elementlar


# uyga vazifa

# sonlar = []

# for i in range(10):
#     sonlar.append(int(input("son kiriting: ")))

# print(f"Ro'yxat: {sonlar}")
# print(f"Ro'yxat uzunligi: {len(tuple(sonlar))}")

# print(f"Tuple: {tuple(sonlar)}")
# print(f"Tuple uzunligi: {len(sonlar)}")

# set_1 = set(sonlar)
# print(f"Set: {set_1}")
# print(f"Set uzunligi {len(set_1)}")

