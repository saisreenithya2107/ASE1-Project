from django.db import models
# Create your models here.

class Category(models.Model):
    CATEGORY_CHOICES = (
        ('Hostel', 'Hostel'),
        ('Lab', 'Lab'),
        ('Books', 'Books'),
    )
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.category

    def __repr__(self):
        return self.category

class Products_Selling(models.Model):
    pname = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    photo = models.ImageField(upload_to='SellingProductsPhotos/')
    Category = models.ForeignKey('Category', on_delete=models.CASCADE)
    Seller = models.ForeignKey("registration.Profile", on_delete=models.CASCADE)
    amount = models.FloatField(null=False, blank=False)

    def __str__(self):
        return self.pname

    def __repr__(self):
        return self.pname