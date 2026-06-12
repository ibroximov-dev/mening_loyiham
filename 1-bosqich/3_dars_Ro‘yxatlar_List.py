# Lict "ro'yxat!"
# 1. Ro‘yxat yaratish
# ism = ["Ali", "Vali", "Hasan"]
# sonlar = [1,2,3,4,5,6]
# aralash = ["Ali", 7, 1.72, True]
# print(ism)
# print(sonlar)
# print(aralash)

# 2. Indeks (nomerlash)
# Ro‘yxatda 0 dan boshlab nomerlanadi:
# ism = ["Ali", "Vali", "Hasan"]
# print(ism[0])
# print(ism[1])
# print(ism[2])

# print(ism[-1])
# print(ism[-2])

# 3. Ro‘yxatni o‘zgartirish
# ismlar = ["Ali", "Vali", "Hasan"]
# ismlar.append("Olim")
# print(ismlar)

# ismlar.insert(2,"Olim")
# print(ismlar)

# ismlar.remove("Vali")
# print(ismlar)

# ochirilganlar = ismlar.pop()
# print(ochirilganlar)
# print(ismlar)

# ismlar[0] = "Anvar"
# print(ismlar)

# 4. Ro‘yxatdan ma’lumot olish
# sonlar = [10,20,30,40,50,60]

# print(len(sonlar))

# if 30 in sonlar:
#     print("30 soni bor ekan")

# index = sonlar.index(40)
# print(index)
# print(sonlar[0:3])   # [10, 20, 30] (0 dan 3 gacha, 3 kirmaydi)
# print(sonlar[2:])    # [30, 40, 50, 60] (2 dan oxirgacha)
# print(sonlar[:4])    # [10, 20, 30, 40] (boshidan 4 gacha)
# print(sonlar[::2])   # [10, 30, 50] (2 qadam bilan)


# 5. Foydali ro‘yxat metodlari
# sonlar = [3, 1, 4, 1, 5, 9, 2]
# sonlar.sort()
# print(sonlar)

# sonlar.reverse()
# print(sonlar)

# print(sonlar.count(1))

# sonlar.clear()
# print(sonlar)

# uyga vazifa

# ism1 = input("Ism kiriting: ") 
# ism2 = input("Ism kiriting: ") 
# ism3 = input("Ism kiriting: ") 
# ism4 = input("Ism kiriting: ") 
# ism5 = input("Ism kiriting: ") 
# ismlar = [ism1,ism2,ism3,ism4,ism5]

# qidiruv = input("Qidirayotgan ismingiz: ")
# if qidiruv in ismlar:
#     natija = (f"{qidiruv} ro‘yxatda  {ismlar.index(qidiruv) + 1}-indeksda")
#     print(natija)
# else:
#     natija = input(f"{qidiruv} ro‘yxatda yo‘q. Qo‘shishni xohlaysizmi? (ha/yo‘q): ")
#     if natija == "ha":
#         ismlar.append(qidiruv)
#         print(f"Yangi ro'yxat: {ismlar}")
#     else:
#         print("Siz aytgan ismni qo'shmadik!")
        

# ismlar.sort()
# print(f"Tartiblangan: {ismlar}")