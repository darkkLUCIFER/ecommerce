from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import LoginForm, RegisterForm, EditUserForm
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


@login_required(login_url='/login')
def user_profile(request):
    user_full = request.user
    context = {
        'user_full': user_full
    }
    return render(request, 'account/user_profile.html', context)


@login_required(login_url='/login')
def edit_user_profile(request):
    user_id = request.user.id
    user = User.objects.get(id=user_id)
    if user:
        form = EditUserForm(data=request.POST or None,
                            initial={'first_name': user.first_name, 'last_name': user.last_name})
        if form.is_valid():
            cd = form.cleaned_data
            first_name = cd['first_name']
            last_name = cd['last_name']
            user.first_name = first_name
            user.last_name = last_name
            user.save()
        return render(request, 'account/edit_user_profile.html', {'form': form})


def user_profile_sidebar(request):
    context = {}
    return render(request, 'account/user_profile_sidebar.html', context)
