from django.db import models


# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=128)
    price = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return f"{self.title, self.id}"
