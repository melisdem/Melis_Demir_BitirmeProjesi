from django.shortcuts import render

# view fonksiyonumuzun html kodlarını response olarak döndürecek fonksiyonu import ediyoruz
from django.http import HttpResponse
# html template'ini response olarak döndürebilmek için ise render'ı import ediyoruz
from django.shortcuts import render
# forms.py de oluşturduğumuz formu import ediyoruz ki contact'ın url'sini çağırdığımızda onunla bağlantı kurabilelim
from .forms import ContactForm



# Create your views here.

# app'im olan home dosyası içinde templates dosyası oluşturuyorum
# templates içinde de home klasörü oluşturuyorum ki farklı app'leirmin içinde aynı isimli html dosyaları olursa
# django bunları karıştırmasın, klasör yolumuzdan anlaşılsın, karışıklık olmasın
# render(request, "home/index.html") templates içinde home içinde index dosyası


# http://127.0.0.1:8000 sayfasında ne yapıcağımızı göstermek için
def index(request):
    return render(request, "home/index.html")

# http://127.0.0.1:8000/about sayfasında ne yapıcağımızı göstermek için

def about(request):
    return render(request, "home/about.html")

# django dökümantasyonuna göre formları view fonksiyonlarında aşağıdaki gibi çağırabiliriz
# from .forms import NameForm
#
#
# def get_name(request):
#     # if this is a POST request we need to process the form data
#     if request.method == "POST":
#         # create a form instance and populate it with data from the request:
#         form = NameForm(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required
#             # ...
#             # redirect to a new URL:
#             return HttpResponseRedirect("/thanks/")
#
#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = NameForm()
#
#     return render(request, "name.html", {"form": form})

# {"form": form} yerine ben contextData yaptım ki sözlük de kullanmış olalım

# özetle eğer POST edilmiş bir form varsa bunu requestten al ContactForm'da düzenle
# eğer valid'se database'e kaydet ve formu temizle ki mesaj gitsin, yeniden başka mesaj gönderilebilsin
# eğer post edilmiş bir şey yoksa boş bir form oluştur bekle

# http://127.0.0.1:8000/contact sayfasında ne yapıcağımızı göstermek için
def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST) # forms.py de oluşturduğumuz ContactForm classını requestten aldığımız datalarla doldur ve bunu form değişkenine ata
        if form.is_valid(): # is_valid ve.save() metodları djangonun içinde kayıtlı metodlar bu sebeple djangoda databaselerle çalışmak kolaylaşıyor
            form.save()
            form = ContactForm()
            reply = "Mesajınız için teşekkürler, en kısa sürede dönüş yapılacaktır"
            return render(request, "home/contact.html", {"form":form, "reply":reply})
    else:
        form = ContactForm()

    contextData = {
        "form": form
    }
    return render(request, "home/contact.html", contextData)

def mercimek(request):
    return render(request,"home/mercimek.html")
def dolma(request):
    return render(request, "home/dolma.html")
def pizza(request):
    return render(request, "home/pizza.html")
def sekerpare(request):
    return render(request,"home/sekerpare.html")


