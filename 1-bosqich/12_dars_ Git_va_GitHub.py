# 📘 Git va GitHub — sodda tushuntirish
# Git nima?
# Git — bu versiya boshqarish tizimi. Har bir o'zgarishingizni xotirlaydi va kerak bo'lsa oldingi holatga qaytarish imkonini beradi.

# GitHub nima?
# GitHub — bu bulutda Git. Kodingizni internetda saqlaysiz, boshqalar bilan bo'lishasiz, jamoada ishlaysiz.

# Oddiy misol:
# Tasavvur qiling: siz insho yozyapsiz.

# Git — "so'nggi 10 ta o'zgarishni eslab qolaman, istagan vaqtda eski versiyaga qaytish mumkin"

# GitHub — "bu inshoni internetga yuklaysiz, do'stlaringiz bilan bo'lishishingiz va birgalikda yozishingiz mumkin"

# 🎯 1-dars: Git o'rnatish va asosiy buyruqlar
# 1. Git ni o'rnatish:
# Windows uchun:

# git-scm.com saytiga o'ting

# "Download for Windows" tugmasini bosing

# O'rnatuvchi faylni ishga tushiring (barcha standart sozlamalarni qoldiring)

# O'rnatilganini tekshirish:

# bash
# git --version
# # git version 2.xx.xx chiqsa, tayyor!
# 2. Git ni sozlash (bir marta qilinadi):
# bash
# # Ismingizni yozing
# git config --global user.name "Ismingiz Familiyangiz"

# # Emailingizni yozing (GitHub bilan bir xil bo'lsin)
# git config --global user.email "emailingiz@gmail.com"
# 3. Yangi loyiha boshlash:
# bash
# # Loyiha papkasini yarating
# mkdir mening_loyiha
# cd mening_loyiha

# # Git ombori (repository) yaratish
# git init
# git init — bu papkani Git nazoratiga olish. .git papkasi yaratiladi.

# 4. Asosiy buyruqlar:
# bash
# # 1. Yangi fayl yarating
# echo "print('Salom Git!')" > main.py

# # 2. Faylni Gitga qo'shish (staging area ga)
# git add main.py

# # 3. O'zgarishlarni saqlash (commit)
# git commit -m "Birinchi commit: main.py qo'shildi"

# # 4. Holatni tekshirish
# git status
# 5. Asosiy buyruqlar jadvali:
# Buyruq	Ma'nosi	Qachon ishlatiladi?
# git init	Git omborini yaratish	Yangi loyiha boshlaganda
# git add .	Hamma fayllarni qo'shish	O'zgarishlarni saqlashga tayyorlash
# git add fayl.py	Bitta faylni qo'shish	Faqat ma'lum faylni saqlamoqchi bo'lsangiz
# git commit -m "xabar"	O'zgarishlarni saqlash	"Bu holatni eslab qol" degan ma'noda
# git status	Holatni ko'rsatish	Qanday fayllar o'zgargan?
# git log	Commitlar tarixini ko'rsatish	Kim, qachon, nima o'zgartirgan?
# ✅ Bugungi amaliy topshiriq:
# 1. Git ni o'rnating va sozlang:
# bash
# git --version
# git config --global user.name "Sizning ismingiz"
# git config --global user.email "emailingiz"
# 2. Yangi loyiha yarating:
# bash
# # Papka yarating
# mkdir ~/Desktop/my_first_git
# cd ~/Desktop/my_first_git

# # Git omborini yarating
# git init

# # "salom.py" fayl yarating
# echo "print('Gitni o'rganyapman!')" > salom.py

# # Faylni qo'shing va commit qiling
# git add salom.py
# git commit -m "Birinchi commit: salom.py qo'shildi"

# # Holatni tekshiring
# git status
# 3. Yana bitta fayl qo'shing:
# bash
# # "ism.py" fayl yarating
# echo "ism = 'Sizning ismingiz'" > ism.py

# # Gitga qo'shing
# git add ism.py
# git commit -m "ism.py qo'shildi"

# # Commitlar tarixini ko'ring
# git log
# 📤 Qanday topshirasiz?
# Terminaldan quyidagi buyruqlar natijalarini ko'chirib yuboring:

# bash
# git status
# git log
# Eslatma: Keyingi darsda GitHub ga ulashni va push/pull buyruqlarini o'rganamiz!


# bajarilgan topshiriq:
# PS C:\Users\ibroximov\Desktop\Obsession> cd mening_loyiha
# PS C:\Users\ibroximov\Desktop\Obsession\mening_loyiha> git init
# Initialized empty Git repository in C:/Users/ibroximov/Desktop/Obsession/mening_loyiha/.git/
# PS C:\Users\ibroximov\Desktop\Obsession\mening_loyiha> echo "print('Salom Git!')" > main.py
# PS C:\Users\ibroximov\Desktop\Obsession\mening_loyiha> git add main.py
# PS C:\Users\ibroximov\Desktop\Obsession\mening_loyiha> git commit -m "Birinchi commit: main.py qo'shildi"
# [master (root-commit) a1be39b] Birinchi commit: main.py qo'shildi
#  1 file changed, 0 insertions(+), 0 deletions(-)
#  create mode 100644 main.py
# PS C:\Users\ibroximov\Desktop\Obsession\mening_loyiha> git status
# On branch master
# nothing to commit, working tree clean
# PS C:\Users\ibroximov\Desktop\Obsession\mening_loyiha> git log
# commit a1be39bbb665ef788016cdaebb4fab460df7dfeb (HEAD -> master)
# Author: Ibroximov Isroiljon <isroiljonibroximov2@gmail.com>
# Date:   Fri Jun 12 17:23:50 2026 +0500

#     Birinchi commit: main.py qo'shildi
# PS C:\Users\ibroximov\Desktop\Obsession\mening_loyiha>








