from django.shortcuts import render
from eshop_slider.models import Slider
from eshop_setting.models import SiteSetting


def home_page_view(request):
    sliders = Slider.objects.filter(active=True)
    return render(request, 'home_page.html', {'sliders': sliders})


def header_view(request):
    site_settings = SiteSetting.objects.first()
    context = {'site_settings':site_settings}
    return render(request, 'shared/Header.html', context)


def footer_view(request):
    site_setting = SiteSetting.objects.first()
    context = {'site_setting': site_setting}
    return render(request, 'shared/Footer.html', context)


def about_page(request):
    site_settings = SiteSetting.objects.first()
    context = {'site_settings': site_settings}
    return render(request, 'about_us/about_page.html', context)
