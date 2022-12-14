import time

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from product.models import Product
from .forms import UserNewOrderForm
from .models import OrderDetail, Order

from django.http import HttpResponse, Http404
from zeep import Client


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
            return redirect(f'/product/detail/{product.id}')

    return redirect('ecommerce:home_page')


@login_required(login_url='/login')
def user_open_order(request, *args, **kwargs):
    context = {
        'order': None,
        'detail': None,
        'total': 0
    }
    open_order = Order.objects.filter(owner_id=request.user.id, is_paid=False).first()
    open_order_detail = open_order.orderdetail_set.all()
    if open_order is not None:
        context['order'] = open_order
        context['detail'] = open_order_detail
        context['total'] = open_order.get_total_price()

    return render(request, 'order/user_open_order.html', context)


@login_required(login_url='/login')
def remove_order_detail(request, *args, **kwargs):
    detail_id = kwargs.get('detail_id')
    if detail_id is not None:
        order_detail = OrderDetail.objects.get_queryset().get(id=detail_id, order__owner_id=request.user.id)
        if order_detail is not None:
            order_detail.delete()
            return redirect('eshop_order:user_open_order')
    raise Http404()


MERCHANT = 'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX'
amount = 1000  # Toman / Required
description = "?????????????? ?????????? ???? ???????????? ???? ???? ?????? ???????? ???????? ????????"  # Required
email = 'email@example.com'  # Optional
mobile = '09123456789'  # Optional

client = Client('https://www.zarinpal.com/pg/services/WebGate/wsdl')
CallbackURL = 'http://localhost:8000/verify'  # Important: need to edit for really server.


def send_request(request):
    total_price = 0
    open_order = Order.objects.filter(owner_id=request.user.id, is_paid=False).first()
    if open_order is not None:
        total_price = open_order.get_total_price()
        result = client.service.PaymentRequest(MERCHANT, total_price, description, email, mobile,
                                               f'{CallbackURL}/{open_order.id}')
        if result.Status == 100:
            return redirect('https://www.zarinpal.com/pg/StartPay/' + str(result.Authority))
        else:
            return HttpResponse('Error code: ' + str(result.Status))
    raise Http404()


def verify(request, *args, **kwargs):
    order_id = kwargs['order_id']
    if request.GET.get('Status') == 'OK':
        result = client.service.PaymentVerification(MERCHANT, request.GET['Authority'], amount)
        if result.Status == 100:
            user_order = Order.objects.get_queryset().get(id=order_id)
            user_order.is_paid = True
            user_order.payment_date = time.time()
            user_order.save()
            return HttpResponse('Transaction success.\nRefID: ' + str(result.RefID))
        elif result.Status == 101:
            return HttpResponse('Transaction submitted : ' + str(result.Status))
        else:
            return HttpResponse('Transaction failed.\nStatus: ' + str(result.Status))
    else:
        return HttpResponse('Transaction failed or canceled by user')
