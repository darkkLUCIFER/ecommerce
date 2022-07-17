from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import LoginForm, RegisterForm
from django.contrib.auth.models import User


def login_view(request):
    if request.user.is_authenticated:
        return redirect('ecommerce:home_page')

    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            username = cd['username']
            password = cd['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.success(request, 'با موفقیت وارد شدید.', extra_tags='success')
                    return redirect('ecommerce:home_page')
                else:
                    messages.warning(request, 'اکانت شما غیر فعال است!!! \n برای فعال سازی به ادمین سایت اطلاع دهید.',
                                     extra_tags='warning')
            messages.warning(request, 'اطلاعات هویتی شما در سامانه موجود نمیباشد!!! \n لطفا دوباره ثبتنام کنید.',
                             extra_tags='warning')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


def register_view(request):
    if request.user.is_authenticated:
        return redirect('ecommerce:home_page')

    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            username = cd['username']
            email_address = cd['email_address']
            password = cd['password']
            User.objects.create_user(username=username, email=email_address, password=password)
            messages.success(request, 'اکانت شما با موفقیت ساخته شد', extra_tags='success')
            return redirect('account:login')
    else:
        form = RegisterForm()
    return render(request, 'account/register.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.success(request, 'با موفقیت خارج شدید', extra_tags='success')
    return redirect('ecommerce:home_page')
