from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fname = models.CharField(max_length=100, blank=False)
    lname = models.CharField(max_length=100, blank=False)
    dob = models.DateField(("DOB"), blank=False)
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    rating = models.FloatField(null=False, default=0)
    photo = models.ImageField(upload_to='ProfilePhotos')
    activation_link = models.CharField(max_length=200, null=False)
    bio = models.TextField(max_length=500, blank=True)