# 📘 7-dars: Funksiyalar (def)
# Funksiya — qayta ishlatiladigan kod bo'lagi. Bir marta yozasiz, kerakli joyda chaqirasiz.

# 1. Funksiya yaratish va chaqirish
# def salom_ber():
#     print(f"Salom! Assalomu alaykum")

# salom_ber()


# 2. Parametrlar (ma'lumot qabul qilish)
# Bir parametrli funksiya

# def salom_ber(salom):
#     print(f"Salom {salom}")
# salom_ber("Ali")

# nechta parametrli funksiya
# def salom_ber(ism, familya):
#     print(f"Salom {ism} - {familya}")

# salom_ber("Isroiljon", "Ibroximov")


# 3. Qiymat qaytarish (return)

# def qosh(a,b):
#     return a+b 
# natija = qosh(5,3)
# print(natija)

# return dan keyingi kod ishlamaydi!
# def tekshir(yosh):
#     if yosh >=18:
#         return "katta"
#     return "kichik"
# print(tekshir(20))
# print(tekshir(15))


# 4. Default (standart) qiymatlar
# def salom_ber(ism="mehmon"):
#     print(f"Assalomu alaykum {ism}")
# salom_ber("Isroiljon")
# salom_ber()

# def kopaytir(a, b=2):
#     return a * b 

# print(kopaytir(5))
# print(kopaytir(5,3))


# 5. Bir nechta qiymat qaytarish
# def sonlarni_ayrish_va_qosh(a,b):
#     yigindi = a + b
#     ayrish = a - b
#     return yigindi, ayrish

# natija = sonlarni_ayrish_va_qosh(10,3)
# print(natija)

# y, a = sonlarni_ayrish_va_qosh(10, 3)
# print(f"Yig'indi: {y}, Ayirma: {a}")  # Yig'indi: 13, Ayirma: 7



# 6. Funksiya ichida funksiya
# def katta_son(a,b):
#     def solishtir(x,y):
#         if x > y :
#             return x
#         return y
#     return solishtir(a,b)

# print(katta_son(10,20))



# 7. *args va **kwargs (ixtiyoriy miqdordagi argumentlar)
# def yigindi(*sonlar):
#     natija = 0
#     for son in sonlar:
#         natija += son
#     return natija
# print(yigindi(1,2,3))
# print(yigindi(10,20,30,40))


# **kwargs — ko'p kalit-qiymat argumentlari
# def malumotlar(**kwargs):
#     for kalit, qiymat in kwargs.items():
#         print(f"{kalit} - {qiymat}")

# malumotlar(ism="Ali", yosh=20, shahar="Toshkent")

# 8. Funksiya nima uchun kerak?
# Funksiyasiz	Funksiya bilan
# Kod takrorlanadi	Kod bir marta yoziladi
# O'zgartirish qiyin	Bir joydan o'zgartiriladi
# Katta loyihada chalkash	Modulli va toza kod
# Misol — funksiyasiz:

# python
# # 3 marta bir xil kod
# print("Salom, Ali!")
# print("Salom, Vali!")
# print("Salom, Hasan!")
# Funksiya bilan:

# python
# def salom_ber(ism):
#     print(f"Salom, {ism}!")

# salom_ber("Ali")
# salom_ber("Vali")
# salom_ber("Hasan")


# uyga vazifa
# def kvadrat(a):
#     return a ** 2
# print(kvadrat(5))


# def juftmi(son):
#     if son % 2 == 0:
#         return f"Siz kiritgan {son} juft son!"
#     return f"Siz kiritgan {son} toq son!"


# def faktorial(n):
#     natija = 1
#     for son in range(1,n +1):
#         natija *= son
#     return natija
# print(faktorial(5))


# def talaba_info(ism, yosh, shahar="Toshkent"):
#     return f"{ism}, {yosh} yosh, {shahar}"

# print(talaba_info("Ali", 20))  # Ali, 20 yosh, Toshkent
# print(talaba_info("Vali", 21, "Samarqand"))  # Vali, 21 yosh, Samarqand