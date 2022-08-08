from django import forms
from django.contrib.auth.models import User
from django.core import validators


class LoginForm(forms.Form):
    username = forms.CharField(max_length=25, label='نام کاربری', widget=forms.TextInput)
    password = forms.CharField(max_length=30, label='رمز عبور', widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=25, label='نام کاربری', widget=forms.TextInput, validators=[
        validators.MaxLengthValidator(limit_value=25,
                                      message='تعداد کارکتر های وارد شده نمیتواند بیشتر از 25 کارکتر باشد.'),
        validators.MinLengthValidator(limit_value=2,
                                      message='تعداد کارکتر های وارد شده نمیتواند کمتر از 2 کارکتر باشد.')
    ])
    email_address = forms.EmailField(label='ایمیل', widget=forms.EmailInput)
    password = forms.CharField(max_length=30, label='رمز عبور', widget=forms.PasswordInput)
    re_password = forms.CharField(max_length=30, label='تکرار رمز عبور', widget=forms.PasswordInput)

    def clean_re_password(self):
        password = self.cleaned_data['password']
        re_password = self.cleaned_data['re_password']
        if password != re_password:
            raise forms.ValidationError('رمز عبور های وارد شده با هم تطابق ندارند')
        if len(password) < 8:
            raise forms.ValidationError('تعداد کارکتر های مجاز برای رمز عبور حداقل 8 کارکتر میباشد')
        return password

    def clean_username(self):
        username = self.cleaned_data['username']
        username_exist = User.objects.filter(username=username).exists()
        if username_exist:
            raise forms.ValidationError('این نام کاربری انتخاب شده است!!!')

        return username

    def clean_email_address(self):
        emai_address = self.cleaned_data['email_address']
        email_exist = User.objects.filter(email=emai_address).exists()
        if email_exist:
            raise forms.ValidationError('این ایمیل قبلا استفاده شده است!!!')

        if len(emai_address) < 10:
            raise forms.ValidationError('تعداد کارکتر های ایمیل نمیتواند از 10 کارکتر کمتر باشد.')

        if len(emai_address) > 30:
            raise forms.ValidationError('تعداد کارکتر های ایمیل بیش از حد میباشد.')

        return emai_address


class EditUserForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput, label='نام')
    last_name = forms.CharField(widget=forms.TextInput, label='نام خانوادگی')
