from django.db import models
# Create your models here.

class Category(models.Model):
    CATEGORY_CHOICES = (
        ('Hostel', 'Hostel'),
        ('Lab', 'Lab'),
        ('Books', 'Books'),
    )
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)

class Products_Selling(models.Model):
    pname = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    photo = models.ImageField(upload_to='Selling Products Photos')
    Category = models.ForeignKey('Category', on_delete=models.CASCADE)
    Seller = models.ForeignKey("login.Profile", on_delete=models.CASCADE)
    amount = models.FloatField(null=False, blank=False)