from django import forms
from vendor.models import *
from django.contrib.auth.models import User


class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        exclude = ('user',)


class StateForm(forms.ModelForm):
    class Meta:
        model = State
        exclude = ('user',)


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        exclude = ('user',)


class CabForm(forms.ModelForm):
    class Meta:
        model = Cab
        exclude = ('user',)


class CarTypeForm(forms.ModelForm):
    class Meta:
        model = CarType
        exclude = ('user',)


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)

class UserUpdationForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)

    class Meta:
        model = User
        fields = ["first_name","last_name","email","username"]