from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from product.models import Product
from .forms import UserNewOrderForm
from .models import OrderDetail, Order

from django.http import HttpResponse
import requests
import json


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
def user_open_order(request):
    context = {
        'order': None,
        'detail': None
    }
    open_order = Order.objects.filter(owner_id=request.user.id, is_paid=False).first()
    open_order_detail = open_order.orderdetail_set.all()
    if open_order is not None:
        context['order'] = open_order
        context['detail'] = open_order_detail

    return render(request, 'order/user_open_order.html', context)


MERCHANT = 'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX'
ZP_API_REQUEST = "https://api.zarinpal.com/pg/v4/payment/request.json"
ZP_API_VERIFY = "https://api.zarinpal.com/pg/v4/payment/verify.json"
ZP_API_STARTPAY = "https://www.zarinpal.com/pg/StartPay/{authority}"
amount = 11000  # Rial / Required
description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"  # Required
email = 'email@example.com'  # Optional
mobile = '09123456789'  # Optional
# Important: need to edit for really server.
CallbackURL = 'http://localhost:8000/verify/'


def send_request(request):
    req_data = {
        "merchant_id": MERCHANT,
        "amount": amount,
        "callback_url": CallbackURL,
        "description": description,
        "metadata": {"mobile": mobile, "email": email}
    }
    req_header = {"accept": "application/json",
                  "content-type": "application/json'"}
    req = requests.post(url=ZP_API_REQUEST, data=json.dumps(
        req_data), headers=req_header)
    authority = req.json()['data']['authority']
    if len(req.json()['errors']) == 0:
        return redirect(ZP_API_STARTPAY.format(authority=authority))
    else:
        e_code = req.json()['errors']['code']
        e_message = req.json()['errors']['message']
        return HttpResponse(f"Error code: {e_code}, Error Message: {e_message}")


def verify(request):
    t_status = request.GET.get('Status')
    t_authority = request.GET['Authority']
    if request.GET.get('Status') == 'OK':
        req_header = {"accept": "application/json",
                      "content-type": "application/json'"}
        req_data = {
            "merchant_id": MERCHANT,
            "amount": amount,
            "authority": t_authority
        }
        req = requests.post(url=ZP_API_VERIFY, data=json.dumps(req_data), headers=req_header)
        if len(req.json()['errors']) == 0:
            t_status = req.json()['data']['code']
            if t_status == 100:
                return HttpResponse('Transaction success.\nRefID: ' + str(
                    req.json()['data']['ref_id']
                ))
            elif t_status == 101:
                return HttpResponse('Transaction submitted : ' + str(
                    req.json()['data']['message']
                ))
            else:
                return HttpResponse('Transaction failed.\nStatus: ' + str(
                    req.json()['data']['message']
                ))
        else:
            e_code = req.json()['errors']['code']
            e_message = req.json()['errors']['message']
            return HttpResponse(f"Error code: {e_code}, Error Message: {e_message}")
    else:
        return HttpResponse('Transaction failed or canceled by user')
