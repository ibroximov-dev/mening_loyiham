# def kontakt_qosh(kontaktlar, ism, nomer):

#     lugat = {"ism" : ism, "nomer" : nomer}
#     kontaktlar.append(lugat)
#     print(f"'{ism}' kontaktga qo'shildi!")



# def kontaktlar_royxati(kontaktlar):

#     if len(kontaktlar) == 0:
#         print(f"Hech qanday kontakt yo'q")
#     else:
#         for kontakt in kontaktlar:
#             print(f"{kontakt['ism']} : {kontakt['nomer']}")


# def kontakt_qidir(kontaktlar, ism):

#     topildi = False
#     for kontakt in kontaktlar:
#         if kontakt['ism'] == ism:
#             print(f"{kontakt['ism']} : {kontakt['nomer']}")
#             topildi = True
#             break 
#     if topildi == False:
#         print("Kontakt topilmadi!")

# def kontakt_ochir(kontaktlar, ism):
#     topildi = False
#     for kontakt in kontaktlar:
        
#         if kontakt['ism'] == ism:
#             kontaktlar.remove(kontakt)
#             print(f"'{ism}' kontakt o'chirildi!")
#             topildi = True
#             break
#     if topildi == False:
#         print("Kontakt topilmadi!")

# def main():
#     kontaktlar = []  # [{ism: "Ali", nomer: "991234567"}, ...]
    
#     while True:
#         print("\n=== TELEFON DAFTARI ===")
#         print("1. Kontakt qo'shish")
#         print("2. Kontaktlar ro'yxati")
#         print("3. Kontakt qidirish")
#         print("4. Kontakt o'chirish")
#         print("5. Chiqish")
        
#         tanlov = input("Tanlang (1-5): ")
        
#         if tanlov == "1":
#             ism = input("Ism: ")
#             nomer = input("Telefon raqami: ")
#             kontakt_qosh(kontaktlar, ism, nomer)
        
#         elif tanlov == "2":
#             kontaktlar_royxati(kontaktlar)
        
#         elif tanlov == "3":
#             ism = input("Qidirilayotgan ism: ")
#             kontakt_qidir(kontaktlar, ism)
        
#         elif tanlov == "4":
#             ism = input("O'chiriladigan ism: ")
#             kontakt_ochir(kontaktlar, ism)
        
#         elif tanlov == "5":
#             print("Dastur tugadi!")
#             break
        
#         else:
#             print("Xato! 1-5 oralig'ida tanlang!")

# # Dasturni ishga tushirish
# main()


