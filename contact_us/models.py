from django.db import models


class ContactUs(models.Model):
    full_name = models.CharField(max_length=150, verbose_name='نام و نام خانوادگی')
    email_address = models.EmailField(max_length=100, verbose_name='ایمیل')
    subject = models.CharField(max_length=120, verbose_name='موضوع')
    message = models.TextField(verbose_name='پیغام')
    created = models.DateTimeField(auto_now_add=True, verbose_name='زمان ساخت')
    is_read = models.BooleanField(default=False, verbose_name='خوانده شده')

    def __str__(self):
        return self.subject

    class Meta:
        db_table = 'contact_us'
        verbose_name = 'تماس با ما'
        verbose_name_plural = 'تماس های کاربران'
