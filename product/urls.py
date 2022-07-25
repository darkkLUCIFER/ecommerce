from django.urls import path
from .views import ProudctListView, product_detail_view, SearchProductView, ProductListByCategory, product_categories, \
    Error404View

app_name = 'product'

urlpatterns = [
    path('', ProudctListView.as_view(), name='product_list'),
    path('category/<str:category_name>/', ProductListByCategory.as_view(), name='product_list_by_category'),
    path('detail/<int:pk>/', product_detail_view, name='product_detail'),
    path('search/', SearchProductView.as_view(), name='product_search'),
    path('product_category/', product_categories, name='product_category'),
    path('error/404/', Error404View.as_view(), name='error_404'),


]
