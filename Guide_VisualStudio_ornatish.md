# Visual Studio'ni o'rnatish — talabalar uchun qo'llanma

Bu qo'llanma Visual Studio'ni birinchi marta o'rnatayotgan talabalar uchun. Butun kurs davomida
shu dastur ichida kod yozasiz, shuning uchun to'g'ri o'rnatish juda muhim.

## 1. Qaysi versiyani yuklab olish kerak?

**Visual Studio Community** — talabalar uchun MUTLAQO BEPUL versiya. (Diqqat: Visual Studio **Code**
boshqa, yengilroq dastur — bu kursda to'liq **Visual Studio** kerak, Code emas!)

## 2. Yuklab olish va o'rnatish

1. https://visualstudio.microsoft.com/downloads/ manziliga o'ting.
2. **"Community"** versiyasining "Free download" tugmasini bosing.
3. Yuklangan faylni (`VisualStudioSetup.exe`) ishga tushiring.
4. "Workloads" (ish yuklamalari) oynasi ochiladi — bu yerda qaysi turdagi dasturlash uchun vositalar
   kerakligini tanlaysiz.

## 3. ENG MUHIM QADAM: to'g'ri komponentni tanlash

Workloads ro'yxatida **".NET desktop development"** katagiga BELGI QO'YING.

> Agar bu qadamni o'tkazib yuborsangiz, Visual Studio o'rnatiladi, lekin C# konsol dasturlarini
> yarata olmaysiz — "Console App" varianti ro'yxatda chiqmaydi! Agar shunday bo'lsa, Visual Studio
> Installer'ni qayta oching va shu komponentni qo'shing (4-bo'limga qarang).

Boshqa workload'larni (masalan veb-dasturlash, o'yin dasturlash) HOZIRCHA belgilashning hojati yo'q —
keyinchalik istalgan vaqtda qo'shish mumkin.

Pastdagi **"Install"** tugmasini bosing. O'rnatish 15-40 daqiqa davom etishi mumkin (internet tezligiga
bog'liq) — sabr qiling.

## 4. Agar keyinroq komponent qo'shish kerak bo'lsa

1. Windows qidiruvidan **"Visual Studio Installer"** ni toping va oching.
2. O'rnatilgan Visual Studio yonidagi **"Modify"** (o'zgartirish) tugmasini bosing.
3. ".NET desktop development" ni belgilab, "Modify" ni bosing.

## 5. O'rnatish muvaffaqiyatli bo'lganini tekshirish

1. Visual Studio'ni oching.
2. Birinchi ochilishda Microsoft akkauntingiz bilan kirishni so'rashi mumkin — bu ixtiyoriy, "Not now"
   bosib o'tkazib yuborsangiz ham bo'ladi (yoki bepul akkaunt bilan kiring).
3. Bosh oynada **"Create a new project"** ni bosing.
4. Qidiruv maydoniga "Console App" deb yozing — **"Console App" (C#, ... barchasi uchun)** varianti
   ro'yxatda chiqishi kerak. Agar chiqmasa, 4-bo'limga qayting.
5. Uni tanlab, loyihaga `SinovLoyiha` deb nom bering, "Create" ni bosing.
6. Yashil **▶ (Run)** tugmasini bosing (yoki klaviaturada **F5**) — konsol oynasi ochilib,
   "Hello, World!" chiqishi kerak.

Agar shu natijani ko'rsangiz — hammasi to'g'ri o'rnatilgan, darsga tayyorsiz!

## 6. Tez-tez uchraydigan muammolar

**O'rnatish juda sekin yoki to'xtab qoladi?**
Internet aloqangizni tekshiring, kompyuterni qayta ishga tushirib qayta urinib ko'ring.

**"Console App" varianti ro'yxatda yo'q?**
".NET desktop development" workload'i o'rnatilmagan — 4-bo'limdagi qadamlarni bajaring.

**Dastur ishga tushganda xato chiqsa?**
Xato xabarining AYNAN MATNINI nusxalab, darsda yoki chatda ulashing — xatoni birga hal qilamiz.

**Kompyuterim eski/kuchsiz, Visual Studio sekin ishlayaptimi?**
Boshqa barcha dasturlarni (brauzer, Zoom ortiqcha tablar) yoping — Visual Studio ancha xotira talab qiladi.

## 7. Keyingi qadam

Visual Studio o'rnatilgach, [Guide_GitHub_boshlangich.md](Guide_GitHub_boshlangich.md) qo'llanmasiga
o'ting — u yerda yozgan loyihalaringizni qanday saqlab, o'qituvchingizga ko'rsatishni o'rganasiz.
