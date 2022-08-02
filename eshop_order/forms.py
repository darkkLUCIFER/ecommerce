from django import forms


class UserNewOrderForm(forms.Form):
    product_id = forms.IntegerField(widget=forms.HiddenInput, label='آیدی محصول')
    count = forms.IntegerField(widget=forms.NumberInput, label='تعداد', initial=1)
