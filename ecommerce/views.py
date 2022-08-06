import itertools

from django.shortcuts import render
from eshop_slider.models import Slider
from eshop_setting.models import SiteSetting
from product.models import Product


def my_grouper(n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))


def home_page_view(request):
    sliders = Slider.objects.filter(active=True)
    most_visit_product = Product.objects.order_by('-visit_count').all()[:8]
    latest_product = Product.objects.order_by('-id').all()[:8]
    context = {
        'sliders': sliders,
        'most_visit': my_grouper(4, most_visit_product),
        'latest_product': my_grouper(4,latest_product),

    }
    return render(request, 'home_page.html', context)


def header_view(request):
    site_settings = SiteSetting.objects.first()
    context = {'site_settings': site_settings}
    return render(request, 'shared/Header.html', context)


def footer_view(request):
    site_setting = SiteSetting.objects.first()
    context = {'site_setting': site_setting}
    return render(request, 'shared/Footer.html', context)


def about_page(request):
    site_settings = SiteSetting.objects.first()
    context = {'site_settings': site_settings}
    return render(request, 'about_us/about_page.html', context)
