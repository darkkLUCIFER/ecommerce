from django.urls import path

from eshop_order.views import add_user_order

app_name = 'eshop_order'

urlpatterns = [
    path('add_user_order/', add_user_order, name='add_user_order'),


]
