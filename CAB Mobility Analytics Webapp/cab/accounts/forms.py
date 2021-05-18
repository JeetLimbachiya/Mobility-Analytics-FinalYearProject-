from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User  
from django import forms
from accounts.models import CreateUser, CabPredictionModel, Contact


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)

    class Meta:
        model = User
        fields = ["first_name","last_name","email","username","password1","password2"]

    def save(self, commit=True):
        user = super().save(commit=False)

        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()
        return user


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = CreateUser
        fields = ["user_acc"]


class CabPredictionForm(forms.ModelForm):
    class Meta:
        model = CabPredictionModel
        fields = '__all__'

class ContactUs(forms.ModelForm):
    name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)
    subject = forms.CharField(max_length=250)
    message = forms.CharField(max_length=500)

    class Meta:
        model = Contact
        fields = ["name","email","subject","message"]

    def save(self, commit=True):
        contactus = super().save(commit=False)

        contactus.email = self.cleaned_data['email']
        contactus.name = self.cleaned_data['name']
        contactus.subject = self.cleaned_data['subject']
        contactus.message = self.cleaned_data['message']

        if commit:
            contactus.save()
        return contactus
