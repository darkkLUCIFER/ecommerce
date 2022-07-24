from django.shortcuts import render
from eshop_slider.models import Slider


def home_page_view(request):
    sliders = Slider.objects.filter(active=True)
    return render(request, 'home_page.html', {'sliders':sliders})

# <--render_partial_views-->
# def header_view(request):
#     context = {}
#     return render(request, 'shared/Header.html', context)
#
#
# def footer_view(request):
#     context = {}
#     return render(request, 'shared/Footer.html', context)
# <--/render_partial_views-->
