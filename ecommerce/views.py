from django.shortcuts import render


def home_page_view(request):
    return render(request, 'home_page.html')


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
