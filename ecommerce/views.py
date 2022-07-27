from django.shortcuts import render
from eshop_slider.models import Slider
from eshop_setting.models import SiteSetting


def home_page_view(request):
    sliders = Slider.objects.filter(active=True)
    return render(request, 'home_page.html', {'sliders': sliders})


def header_view(request):
    context = {}
    return render(request, 'shared/Header.html', context)


def footer_view(request):
    site_setting = SiteSetting.objects.first()
    context = {'site_setting': site_setting}
    return render(request, 'shared/Footer.html', context)
