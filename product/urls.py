from django.urls import path
from .views import ProudctListView, product_detail_view

app_name = 'product'

urlpatterns = [
    path('', ProudctListView.as_view(), name='product_list'),
    path('<int:pk>/', product_detail_view, name='product_detail'),

]
