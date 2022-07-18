from django.shortcuts import render
from .models import Product
from django.views.generic import ListView


class ProudctListView(ListView):
    model = Product
    template_name = 'product/products_list.html'
    queryset = Product.objects.filter(active=True)
    context_object_name = 'products'
    paginate_by = 1

# def product_list(request):
#     products = Product.objects.all()
#     return render(request, 'product/products_list.html', {'products': products})
