# 📘 1. Git nima?
# Git — versiya boshqarish tizimi. Har bir o'zgarishingizni xotirlaydi.

# GitHub — Git omborlarini internetda saqlaydigan platforma.

# 📘 2. O'rnatish va sozlash
# bash
# # O'rnatilganini tekshirish
# git --version

# # Ism va email sozlash (bir marta)
# git config --global user.name "Ismingiz"
# git config --global user.email "emailingiz@gmail.com"
# 📘 3. Asosiy buyruqlar
# Buyruq	Vazifasi
# git init	Yangi Git ombori yaratish
# git status	Holatni ko'rsatish
# git add .	Hamma o'zgarishlarni qo'shish
# git add fayl.py	Bitta faylni qo'shish
# git commit -m "xabar"	O'zgarishlarni saqlash
# git log	Commitlar tarixini ko'rish
# git remote add origin URL	GitHub bilan ulash
# git push	GitHub ga yuklash
# git pull	GitHub dan yuklab olish
# git clone URL	GitHub dan loyihani nusxalash
# 📘 4. Ish jarayoni (1-kun)
# bash
# # 1. Loyiha papkasiga o'tish
# cd ~/Desktop/mening_loyiham

# # 2. Git ombori yaratish
# git init

# # 3. Fayl yaratish
# echo "print('Salom')" > main.py

# # 4. Faylni qo'shish
# git add main.py

# # 5. Commit qilish
# git commit -m "Birinchi commit"

# # 6. GitHub da repository yaratish
# # (Veb-sayt orqali)

# # 7. GitHub ga ulash
# git remote add origin https://github.com/username/repo.git

# # 8. Yuklash
# git branch -M main
# git push -u origin main
# 📘 5. Ish jarayoni (keyingi kunlar)
# bash
# # 1. O'zgarish qilish (fayllarni tahrirlash)

# # 2. O'zgarishlarni qo'shish
# git add .

# # 3. Commit qilish
# git commit -m "Nima o'zgargani haqida"

# # 4. GitHub ga yuklash
# git push
# 📘 6. GitHub dan loyihani olish
# bash
# # Birinchi marta (clone)
# git clone https://github.com/username/repo.git

# # Keyingi marta (yangilash)
# git pull
# 📘 7. Branch va Merge (tarmoqlar)
# bash
# # Yangi branch yaratish
# git branch yangi_xususiyat

# # Branch ga o'tish
# git checkout yangi_xususiyat

# # Yoki bir vaqtda yaratish va o'tish
# git checkout -b yangi_xususiyat

# # O'zgarish qilish va commit
# git add .
# git commit -m "Yangi xususiyat qo'shildi"

# # Asosiy branch ga qaytish
# git checkout main

# # Branch ni birlashtirish
# git merge yangi_xususiyat
# 📘 8. Muhim eslatmalar
# Har kuni commit qiling — bu sizning rezyumeingiz

# Commit xabarini aniq yozing — "main.py yangilandi"

# Push qilishdan oldin pull qiling — git pull then git push

# .git papkasini o'chirmang — u Git ombori

# 📘 9. Tez-tez ishlatiladigan ketma-ketlik
# bash
# git status                 # Holatni tekshir
# git add .                  # Hammani qo'sh
# git commit -m "yangilandi" # Saqla
# git push                   # Yukla
# 📘 10. Xatoliklar va yechimlari
# Xato	Yechim
# nothing to commit	O'zgarish qiling yoki git pull
# remote origin already exists	git remote remove origin
# failed to push	Avval git pull qiling
# merge conflict	Ikkala versiyani qo'lda birlashtirish