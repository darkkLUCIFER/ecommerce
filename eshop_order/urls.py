from django.urls import path

from eshop_order.views import add_user_order, user_open_order, send_request, verify

app_name = 'eshop_order'

urlpatterns = [
    path('add_user_order/', add_user_order, name='add_user_order'),
    path('user_open_order/', user_open_order, name='user_open_order'),
    path('request/', send_request, name='request'),
    path('verify/<int:order_id>/', verify, name='verify'),

]
