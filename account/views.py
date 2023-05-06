from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.

def loginUser(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            ContextData = {
                "error": "Kullanıcı adı veya parola hatalıdır. Lütfen tekrar deneyiniz"
            }
            return render(request, "account/login.html", ContextData)
    else:
        return render(request, "account/login.html")

def registerUser(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]

            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, ("Tebrikler!, Kaydınız oluşturulmuştur"))
            return redirect("home")
    else:
        form = UserCreationForm()
    return render(request, "account/register.html", {"form":form})


def logoutUser(request):
    logout(request)
    messages.success(request,("Çıkış yaptınız, tekrar bekleriz.."))
    return redirect("home")