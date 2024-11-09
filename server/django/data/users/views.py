
from pprint import pprint
from testsite.utils import *
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from .forms import *


# Create your views here.
def sign_up(request):
    if request.POST:
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            authenticate(request, username=user.username, password=user.password)
            login(request, user)
            set_last_user(user)
            save_theme_to_user(user)
            return redirect('home')
    else:
        form = RegisterForm()
    context = {
        'title': "Страница регистрации",
        'form': form,
        'button_text': "Зарегистрироваться"
    }
    
    return render(request, "pawnshop/form.html", context)


def sign_in(request):
    if request.POST:
        form = LoginForm(request.POST)
        print(form.__dict__)
        if form.is_valid():
            print("valid")
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            print(username, password)
            user = authenticate(request, username=username, password=password)
            print(user)
            if user:
                login(request, user)
                set_last_user(user)
                return redirect('home')
            form.add_error(None, "Ошибка входа")
    else:
        form = LoginForm()
    context = {
        'title': "Страница авторизации",
        "form": form,
        "button_text": "Войти"
    }
    
    return render(request, "pawnshop/form.html", context)


def sign_down(request):
    logout(request)
    return redirect('home')


def settings(request):
    print(request.user)
    if request.POST:
        form = SettingsForm(request.POST)
        if form.is_valid():
            theme = form.cleaned_data['theme']
            save_theme_to_user(request.user, theme)
            return redirect("settings")
    else:
        theme = get_theme_from_redis(request.user)
        form = SettingsForm({'theme': theme})
        username, email = get_last_user()
        
    context = {
        "title": "Настройки",
        "form": form,
        "button_text": "Применить",
        'login': username,
        'email': email
    }
    return render(request, "users/settings.html", context)