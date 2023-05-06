from django.contrib import admin
from .models import Contact
# Register your models here.


# Admin sayfasında nasıl görüneceğini anlamak için
class ContactAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "message"]

# admin'de modelimizi tanıtıyoruz
admin.site.register(Contact, ContactAdmin)

