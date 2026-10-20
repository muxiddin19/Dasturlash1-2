# GitHub bilan ishlashni boshlash — talabalar uchun qo'llanma

Bu qo'llanma GitHub bilan birinchi marta ishlayotgan talabalar uchun. Maqsad — uy vazifalaringizni
qanday saqlab, o'qituvchingizga ko'rsatishni o'rganish. Shoshilmang, har bir qadamni ketma-ket bajaring.

## 1. GitHub nima va u nega kerak?

GitHub — dasturchilar o'z kodlarini saqlaydigan, boshqalar bilan ulashadigan va o'zgarishlar tarixini
kuzatib boradigan bepul platforma. Bu kursda siz:
- O'zingizning shaxsiy GitHub **repozitoriyangizni** (repository, qisqacha "repo" — loyihangiz saqlanadigan
  "papka") yaratasiz.
- Har bir amaliy mashg'ulotdan keyin bajargan vazifangizni o'sha repoga **yuklaysiz** (push qilasiz).
- O'qituvchingiz sizning repongizga kirib, bajargan ishlaringizni ko'rib, baholaydi.

## 2. GitHub akkaunt ochish

1. https://github.com/signup manziliga o'ting.
2. Email, parol va foydalanuvchi nomi (username) kiriting — username'ni ODDIY va PROFESSIONAL tanlang
   (masalan `dilnoza-861` kabi, "coolboy2010" kabi emas — bu sizning professional profilingiz bo'ladi).
3. Emailingizga kelgan tasdiqlash kodini kiriting.

## 3. Git dasturini kompyuteringizga o'rnatish

Git — GitHub bilan ishlash uchun kerakli dastur (GitHub veb-sayt, Git esa uning "mexanizmi").

1. https://git-scm.com/downloads manziliga o'ting.
2. Windows uchun versiyani yuklab oling va o'rnating (barcha sozlamalarni standart holda qoldiraverish
   mumkin — "Next, Next, Install").
3. O'rnatilganini tekshirish: Visual Studio'dagi kabi, qidiruvdan "Git Bash" dasturini toping va oching.
   Quyidagini yozing va Enter bosing:
   ```
   git --version
   ```
   Versiya raqami chiqsa — muvaffaqiyatli o'rnatilgan.

## 4. Git'ga o'zingizni tanishtirish (BIR MARTA bajariladi)

Git Bash (yoki Visual Studio'ning terminal oynasi)da quyidagilarni yozing (o'z ism-familiyangiz va
emailingizni kiriting):
```
git config --global user.name "Ismingiz Familiyangiz"
git config --global user.email "sizning-emailingiz@misol.com"
```

## 5. O'zingizning "Dasturlash" repongizni yaratish

1. GitHub'ga kiring, yuqori o'ng burchakdagi **"+"** belgisini bosing → **"New repository"**.
2. Repository nomi (Repository name): masalan `Dasturlash1-2` yoki `Dasturlash-vazifalarim`.
3. **Public** (hammaga ochiq) ni tanlang — o'qituvchingiz shu orqali ko'radi.
4. **"Add a README file"** katagiga belgi qo'ying.
5. **"Create repository"** tugmasini bosing.

Tabriklaymiz — endi sizda o'zingizning repongiz bor!

## 6. Repongizni kompyuteringizga "klonlash" (nusxalash)

1. Repo sahifangizda yashil **"Code"** tugmasini bosing, HTTPS havolasini nusxalang
   (masalan `https://github.com/sizning-usernameingiz/Dasturlash1-2.git`).
2. Kompyuteringizda vazifalaringizni saqlamoqchi bo'lgan papkaga o'ting (masalan Hujjatlar papkasi).
3. O'sha papkada Git Bash oching (papka ichida sichqonchaning o'ng tugmasi → "Git Bash Here", yoki
   Visual Studio terminalidan `cd` buyrug'i bilan o'sha papkaga o'ting).
4. Quyidagini yozing (havolangizni qo'yib):
   ```
   git clone https://github.com/sizning-usernameingiz/Dasturlash1-2.git
   ```
5. Endi kompyuteringizda `Dasturlash1-2` nomli papka paydo bo'ladi — bu sizning repongizning nusxasi.

## 7. Har bir amaliy mashg'ulotdan keyin: vazifani yuklash (push qilish)

Har safar yangi amaliy mashg'ulot tugagach, quyidagi qadamlarni bajaring:

1. `Dasturlash1-2` papkangiz ichida, o'sha haftaga mos papka yarating (masalan `week7`), agar hali yo'q
   bo'lsa.
2. Visual Studio'da yozgan loyihangizni (butun papkasini, masalan `Amaliy1_IDKarta`) o'sha `week7`
   papkasi ichiga nusxalang.
3. Git Bash'da `Dasturlash1-2` papkasiga o'ting va quyidagi TO'RTTA buyruqni ketma-ket bajaring:
   ```
   git add .
   git commit -m "1-amaliy mashg'ulot vazifasi"
   git push
   ```
4. Birinchi marta push qilganda GitHub login (username/parol yoki token) so'rashi mumkin — ko'rsatmalarga
   amal qiling.
5. GitHub'dagi repo sahifangizni yangilab ko'ring — fayllaringiz paydo bo'lgan bo'lishi kerak!

## 8. Tez-tez uchraydigan savollar

**"git: command not found" xatosi chiqsa?**
Git to'g'ri o'rnatilmagan — 3-bo'limni qaytadan bajaring, kompyuterni qayta ishga tushiring.

**push qilganda xato chiqsa ("rejected" yoki shunga o'xshash)?**
Avval `git pull` buyrug'ini yozib, so'ng qaytadan `git push` qiling.

**Qaysi fayllarni yuklashim kerak?**
Butun loyiha papkangizni (ichida `.cs` fayl, `.csproj` fayl bo'ladi) — `bin` va `obj` papkalarini
yuklash SHART EMAS (ular avtomatik yaratiladigan vaqtinchalik fayllar).

**Yordam kerak bo'lsa?**
Darsda yoki chatda savol bering — git bilan ishlash boshida hammaga qiyin tuyuladi, lekin tez o'rganiladi!
