from django.urls import path
from .views import ProudctListView

app_name = 'product'

urlpatterns = [
    path('', ProudctListView.as_view(), name='product_list'),

]
