from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from phonenumber_field.formfields import PhoneNumberField

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class ProfileForm(forms.ModelForm):
    fname = forms.CharField(max_length=100, help_text='Required')
    lname = forms.CharField(max_length=100, help_text='Required')
    dob = forms.DateField(help_text='Required')
    phone = PhoneNumberField(help_text='Required')
    photo = forms.ImageField()
    bio = forms.Textarea()

    class Meta:
        model = Profile
        fields = ('fname', 'lname', 'dob', 'phone', 'photo', 'bio')