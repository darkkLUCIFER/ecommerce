from django.urls import path
from .views import contact_us_view

app_name = 'contact_us'

urlpatterns = [
    path('', contact_us_view, name='contact_us'),

]
