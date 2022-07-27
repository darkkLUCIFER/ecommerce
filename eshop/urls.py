"""eshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from ecommerce.views import footer_view, header_view
from product.views import product_categories

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('ecommerce/', include('ecommerce.urls', namespace='ecommerce')),
                  path('account/', include('account.urls', namespace='account')),
                  path('product/', include('product.urls', namespace='product')),
                  path('contact_us/', include('contact_us.urls', namespace='contact_us')),
                  path('footer/', footer_view, name='footer'),
                  path('header/', header_view, name='header'),
                  path('product_category/', product_categories, name='product_category'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
