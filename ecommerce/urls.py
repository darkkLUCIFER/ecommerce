from django.urls import path
from .views import home_page_view, about_page

app_name = 'ecommerce'

urlpatterns = [
    path('', home_page_view, name='home_page'),
    path('about/', about_page, name='about_page'),

]
