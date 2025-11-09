# 🖥 OpenCV Django Web Application

Bu loyiha **Django** va **OpenCV** yordamida yaratilgan web-ilova bo‘lib, foydalanuvchiga rasm va video orqali real-vaqt tahlil qilish imkonini beradi.  
Loyiha asosiy funksiyalari:

- Kamera orqali odamlarni aniqlash (yuz va ko‘zlarni real vaqt rejimida belgilash)
- Rasmlarni tahlil qilish (asosiy ranglar va shakllarni aniqlash)
- Oddiy web interfeys orqali foydalanuvchi bilan oson ishlash

---

## 📦 O‘rnatish

1. Loyiha fayllarini yuklab oling yoki GitHub’dan klon qiling:

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux / macOS:
source venv/bin/activate

git clone https://github.com/MukhammadjonArabov/OpenCV-Django.git
cd OpenCV-Django
pip install -r requirements.txt 
python manage.py migrate 
python manage.py runserver
```
## 🎬 Loyihaning demo videosi

Quyidagi video loyihaning ishga tushirilishini ko‘rsatadi:

<iframe width="600" height="350" src="https://www.youtube.com/embed/OabU3CehGoE" frameborder="0" allowfullscreen></iframe>
