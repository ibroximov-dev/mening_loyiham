# yosh = 17 

# if yosh >= 18:
#     print("Siz voyga yetgansiz!")
# else:
#     print("Siz hali voyaga yetmagansiz!")


# baho = int(input("Ballingizni kiriting(0-100): "))
# if baho >= 90:
#     daraja = "A'lo(5)"
# elif baho >= 75:
#     daraja = "Yaxshi(4)"
# elif baho >= 60:
#     daraja = "Qoniqarli(3)"
# else:
#     daraja = "Qoniqarsiz(2)"

# print(f"sizning darajangiz {daraja}")

# yosh = 20
# pul = 50000

# if yosh >= 18 and pul>=4000:
#     print("Kinoga kiring olasiz  ")

# if yosh < 12 or yosh > 60:
#     print("Chegirma olasiz")


# if not(yosh<18):
#     print("Voyaga yetmagansiz ")


# fasl = int(input("Hozir qaysi oydasiz(raqam bilan kiriting!): "))

# if fasl == 12 or fasl == 1 or fasl == 2:
#     oy = "Qish fasli. Issiq choy iching!"
# elif fasl == 3 or fasl == 4 or fasl == 5:
#     oy = "Bahor fasli. Tabiat uyg'onadi."
# elif fasl == 6 or fasl == 7 or fasl == 8:
#     oy = "Yoz fasli. Dengizga boring!"
# elif fasl == 9 or fasl == 10 or fasl == 11:
#     oy = "Kuz fasli. Chiroyli barglar."
# else:
#     oy = "Xato"    

# print(f"Siz shu fasldasiz {oy}")



# son1 = int(input("Son kiriting: "))
# son2 = int(input("Son kiriting: "))
# son3 = int(input("Son kiriting: "))
# ortasi = (son1+son2+son3)//3
# print(ortasi)

# ball = int(input("Balingizni kiriting(0-100): "))

# if 90 <= ball == 100:
#     daraja = "A"
# elif 80 <= ball <= 89:
#     daraja = "B"
# elif 70 <= ball <=79:
#     daraja = "C"
# elif 60 <= ball <= 69:
#     daraja = "D"
# elif 0 <= ball <= 59:
#     daraja = "F"
# else:
#     daraja = "Olgan ballingizni sonda kiriting!!!"

# print(daraja)
# uyga vazifa 
# 1 masla

# a = int(input("a burchkini kiriting: "))
# b = int(input("b burchkini kiriting: "))
# c = int(input("c burchkini kiriting: "))

# if a == b == c:
#     natija = "Teng tomonli uchburchak"
# elif a == b or a == c or b == c:
#     natija = "Teng yonli uchburchak"
# elif a != b or a != c or b != c:
#     natija = "Turli tomonli uchburchak"
# else:
#     natija = "Bunday uchburchak mavjud emas"

# print(f"Siz kirtitgan uchburchak tomonlari: {natija} ekan")

# 2 masala

# yosh = int(input("Yoshingizni kiriting: "))

# if 0 <= yosh <= 5:
#     natija = "Bepul!"
# elif 6 <= yosh <= 12:
#     natija = "5000 so'm"
# elif 13 <= yosh <= 17:
#     natija = "10000 so'm"
# elif 18 <= yosh <= 60:
#     natija = "15000 so'm"
# else:
#     natija = "Bepul!"

# print(natija)

# 3-masal

# son = int(input("Son kiriting: "))
# if son % 2 == 0 :
#     natija = "Juft"
# else:
#     natija = "Toq"
# print(f"siz kititgan son {natija}")

# 4-masla
# yil = int(input("Yilni kiritng: "))
# if yil % 400 == 0:
#     natija = "Kasbiy yil"
# elif yil % 100 == 0:
#     natija = "Kasbiy yil emas"
# elif yil % 4 == 0:
#     natija = "Kasbiy yil "
# else:
#     natija = "Kasbiy yil emas!"
# print(f"Siz kiritgan yil {natija} ekan")

# 5-masal
# KALKULYATOR
# son1 = float(input("Birinchi sonni kiriting: "))
# son2 = float(input("Ikkinchi sonni kiriting: "))
# amal = input("Amalni kiriting (+, -, *, /, //, %): ")

# if amal == "+":
#     natija = son1 + son2
# elif amal == "-":
#     natija = son1 - son2
# elif amal == "*":
#     natija = son1 * son2
# elif amal == "/":
#     if son2 != 0:
#         natija = son1 / son2
#     else:
#         natija = "Xato! 0 ga bo'lish mumkin emas"
# elif amal == "//":
#     if son2 != 0:
#         natija = son1 // son2
#     else:
#         natija = "Xato! 0 ga bo'lish mumkin emas"
# elif amal == "%":
#     if son2 != 0:
#         natija = son1 % son2
#     else:
#         natija = "Xato! 0 ga bo'lish mumkin emas"
# else:
#     natija = "Xato! Noto'g'ri amal"

# print(f"Natija: {natija}")