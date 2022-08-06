import itertools

from django.shortcuts import render, redirect
from django.http import Http404

from eshop_order.forms import UserNewOrderForm
from .models import Product, ProductGallery
from django.views.generic import ListView, TemplateView
from product_category.models import ProductCategory


class ProductListView(ListView):
    model = Product
    template_name = 'product/products_list.html'
    queryset = Product.objects.filter(active=True)
    context_object_name = 'products'
    paginate_by = 6


class ProductListByCategory(ListView):
    model = Product
    template_name = 'product/products_list.html'
    context_object_name = 'products'
    paginate_by = 6

    def get_queryset(self):
        category_name = self.kwargs['category_name']
        category = ProductCategory.objects.filter(title__iexact=category_name).first()
        if category is None:
            raise Http404('صفحه مورد نظر یافت نشد.')
        return Product.objects.filter(active=True).filter(categories__title__iexact=category)


def my_grouper(n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))


def product_detail_view(request, **kwargs):
    pk = kwargs['pk']
    form = UserNewOrderForm(request.POST or None, initial={'product_id': pk})
    galleries = ProductGallery.objects.filter(product_id=pk)
    grouped_galleries = list(my_grouper(3, galleries))

    try:
        product = Product.objects.get(active=True, id=pk)
    except Product.DoesNotExist:
        return render(request, 'partials/404.html')
    product.visit_count += 1
    product.save()
    related_products = Product.objects.filter(categories__product=product).distinct()
    grouped_related_products = my_grouper(3, related_products)
    return render(request, 'product/product_detail.html', {'product': product, 'grouped_galleries': grouped_galleries,
                                                           'grouped_related_products': grouped_related_products,
                                                           'form': form})


class SearchProductView(ListView):
    model = Product
    template_name = 'product/products_list.html'
    context_object_name = 'products'
    paginate_by = 6

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q')
        if query:
            return Product.objects.search(query)
        return Product.objects.filter(active=True)


def product_categories(request):
    categories = ProductCategory.objects.all()
    return render(request, 'product/product_category.html', {'categories': categories})


class Error404View(TemplateView):
    template_name = 'partials/404.html'
