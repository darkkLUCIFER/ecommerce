from django.urls import path
from .views import home_page_view

app_name = 'ecommerce'

urlpatterns = [
    path('', home_page_view, name='home_page'),
    # path('header/', header_view, name='header'),
    # path('footer/', footer_view, name='footer'),

]
