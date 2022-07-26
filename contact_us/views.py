from django.contrib import messages
from django.shortcuts import render
from .forms import ContactUsForm
from .models import ContactUs


def contact_us_view(request):
    if request.method == "POST":
        form = ContactUsForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            full_name = cd['full_name']
            email_address = cd['email_address']
            subject = cd['subject']
            message = cd['message']
            ContactUs.objects.create(full_name=full_name, email_address=email_address, subject=subject, message=message)
            messages.success(request, 'پیغام شما با موفقیت ارسال شد', extra_tags='success')

        else:
            messages.warning(request, 'مشکلی در ارسال پیغام شما بوجود آمده است!!!', extra_tags='warning')
    else:
        form = ContactUsForm()
    return render(request, 'contact_us/contact.html', {'form': form})
