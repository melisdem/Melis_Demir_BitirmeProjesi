from django import forms
from .models import Contact

# Djangonun dökümantasyonuna göre
# django formlarla datayı render edebilecek hale getirip
# data için direk html formu hazırlayıp
# submit edilen formları ve datayı clienttan alıp işliyor
# yine dökümantasyonun belirttiğine göre bunu bir çok programcının yapacağından daha güvenli bir şekilde otomatik olarak hazırlıyor

# burada bir form class'ı oluşturuyoruz
# bunu da ModelForm adlı tanımlı Django class'ından alıyoruz
# direk "Form" dan almıyoruz çünkü biz model oluşturduk
# model ve html formu arasında bağlantı kurabilmek için bu class'ı yapıyoruz
# modelForm dökümantasyonuna giderek bu class'ı nasıl oluşturacağımıza bakıyoruz
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "email", "message"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "İsim"}),
            "email": forms.EmailInput(attrs={"placeholder": "Email"}),
            "message": forms.Textarea(attrs={"placeholder": "Lütfen mesajınızı yazınız"})
        }


# bu formu html sayfamızla bağlantılayabilmek için views dosyasında tanımlamamız gerekli
# bu classtan çekeceğimiz {{ form }} değişkeni ile html de django kendisi <input type="text" name="name" id="name" value="" placeholder="İsim"/> elementini oluşturacak
# bu html elementinin stilini kontrol edebilmek için de widgetları kullanıyoruz