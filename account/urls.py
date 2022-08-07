from django.urls import path
from .views import login_view, register_view, logout_view, user_profile, edit_user_profile

app_name = 'account'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('user_profile/', user_profile, name='user_profile'),
    path('edit_user_profile/', edit_user_profile, name='edit_user_profile'),

]
