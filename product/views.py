from django.shortcuts import render
from django.http import Http404
from .models import Product
from django.views.generic import ListView


class ProudctListView(ListView):
    model = Product
    template_name = 'product/products_list.html'
    queryset = Product.objects.filter(active=True)
    context_object_name = 'products'
    paginate_by = 1


def product_detail_view(request, pk):
    try:
        product = Product.objects.get(active=True, id=pk)
    except Product.DoesNotExist:
        return render(request, 'partials/404.html')
    return render(request, 'product/product_detail.html', {'product': product})


class SearchProductView(ListView):
    model = Product
    template_name = 'product/products_list.html'
    context_object_name = 'products'
    paginate_by = 6

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q')
        if query:
            return Product.objects.filter(active=True, title__icontains=query)
        return Product.objects.filter(active=True)
