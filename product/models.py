from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    price = models.PositiveIntegerField()
    image = models.ImageField(null=True, blank=True, upload_to='products/')
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.title
