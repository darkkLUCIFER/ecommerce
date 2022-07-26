from django import forms
from django.core import validators

from .models import ContactUs


class ContactUsForm(forms.Form):
    full_name = forms.CharField(widget=forms.TextInput, label='نام و نام خانوادگی', validators=[
        validators.MaxLengthValidator(150, 'نام شما نمیتواند بیش از 150 کارکتر باشد.')])
    email_address = forms.EmailField(widget=forms.EmailInput, label='ایمیل', validators=[
        validators.MaxLengthValidator(100, 'ایمیل شما نمیتواند بیش از 100 کارکتر باشد.')])
    subject = forms.CharField(widget=forms.TextInput, label='موضوع', validators=[
        validators.MaxLengthValidator(120, 'موضوع شما نمیتواند بیش از 120 کارکتر باشد.')])
    message = forms.CharField(widget=forms.Textarea, label='پیغام')
