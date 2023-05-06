from django.urls import path

# aslında aynı dosya içinde oldukları için from . yaparak dışarı çıkıyormuşuz gibi oluyor
# fakat django önce kendi oluşturduğu dosya/class isimlerine öncelik veriyor
# views dosyasını "import views" dersek kendi oluşturduğu views dosyasına yönlendirecek
# bu yüzden kendi bulunduğumuz dosyadaki views olarak belirtiyoruz
from . import views
# demek oluyor ki views.index için mesela,
# views dosyasına git index fonksiyonunu çalıştır
# views dosyasının hangi dosya olduğunu anlatabilmek için import ediyoruz

# burada home app'i içinde hangi sayfalara yönlnedireceğimizi tanımlıyoruz.
# aynı şekilde ana projemiz olan myproject içinde urls.py dosyasında da home app'ini hangi url ile çağıracağımızı tanımlıyoruz

urlpatterns = [
    path('', views.index, name="home"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('mercimek/', views.mercimek, name="mercimek"),
    path('dolma/', views.dolma, name="dolma"),
    path('pizza/', views.pizza, name="pizza"),
    path('sekerpare/', views.sekerpare, name="sekerpare")
]