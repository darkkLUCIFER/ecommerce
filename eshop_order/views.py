from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from product.models import Product
from .forms import UserNewOrderForm
from .models import OrderDetail, Order


@login_required(login_url='/login')
def add_user_order(request):
    if request.method == "POST":
        form = UserNewOrderForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            product_id = cd['product_id']
            count = cd['count']
            if count < 0:
                count = 1
            product = Product.objects.get(id=product_id)
            order = Order.objects.filter(owner_id=request.user.id, is_paid=False).first()
            if order is None:
                order = Order.objects.create(owner_id=request.user.id, is_paid=False)

            order.orderdetail_set.create(product_id=product.id, price=product.price, count=count)
            # todo : redirect user to user panel
            # return redirect('product:product_detail')

    return redirect('ecommerce:home_page')
