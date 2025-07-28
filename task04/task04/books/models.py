from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200, unique=True)
    author = models.CharField(max_length=100)
    published = models.DateField(null=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title