from django.db import models

# Modeller bizim database'de data'mızı nasıl saklayacağımızın iskeletini oluşturduğumuz class'lar
# Her bir model django.db.models.Model subclass'ının bir Python class'ı
# modellerin her attribute'u database field'ına karşılık oluyor
# Django bize bu modelle otomatik olarak oluşturulmuş bir data sunuyor
# bu dataları sonra database'imizde kullanabiliyoruz ve hatta direk django da bu verileri değiştirip, kaydedip, silebiliyoruz
# Create your models here.

class Contact(models.Model):
    # Model'imizin alanlarını belirtiyoruz.
    # Her model alanı bir class attribute aslında ve bunlar database'e map edilebilir
    # burada da CharField dediğimizde string bir alan oluşturacağız demek oluyor
    # aynı şekilde textField ve EmailField
    name = models.CharField(max_length=80)
    email = models.EmailField()
    message = models.TextField()


# myproject içindeki settings.py dosyasına bakacak olursak DATABASES diye bir tanım var
# içinde         'ENGINE': 'django.db.backends.sqlite3',
#                'NAME': BASE_DIR / 'db.sqlite3', olarak tanımlı iki şey var
# Django dökümantasyonuna göre; django default olarak sqlite3 kullanıyor ve engine'da o tanımlı
# eğer projemizin database'i büyürse ve daha scalable bir database kullanmak istersek mesela mySQL veya PostgreSql gibi
# 'django.db.backends.postgresql', 'django.db.backends.mysql', or 'django.db.backends.oracle' yazarak kullandığımız database'i değiştirebiliriz


# When you add new apps to INSTALLED_APPS, be sure to run manage.py migrate, optionally making migrations for them first with manage.py makemigrations.
# Yine dökümantasyona göre bu modeli oluşturduktan sonra terminalde manage.py makemigrations kodunu çalıştırmalıyız
# terminal Create model Contact diyor ve bize migration dosyası içinde 0001_initial.py diye bir dosya oluşturuyor
# daha sonra da manage.py migrate kodunu terminalde çalıştırıyoruz
# bu django admin'inin tablolarını da, home da oluşan model tablosunu da bizim oluşturuyor
# daha sonra forms.py dosyasını home app'inin altında oluşturuyoruz
# açıklamaları ilgili dosyaya yazdım
