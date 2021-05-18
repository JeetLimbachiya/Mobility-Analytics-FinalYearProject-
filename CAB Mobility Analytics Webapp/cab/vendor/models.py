from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User


class Country(models.Model):
    country_name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.country_name


class State(models.Model):
    state_name = models.CharField(max_length=50)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.state_name


class City(models.Model):
    city_name = models.CharField(max_length=50)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.city_name


class CabSpac(models.Model):
    cab_spac = models.CharField(max_length=50)

    def __str__(self):
        return self.cab_spac


class CarType(models.Model):
    car_type = models.ForeignKey(CabSpac, null=True, on_delete=models.SET_NULL, blank=True)
    car = models.CharField(max_length=50)
    vehicle_no = models.CharField(max_length=50)
    no_of_seat = models.CharField(max_length=50)
    car_model_no = models.CharField(max_length=20)
    per_km_price = models.PositiveSmallIntegerField()
    image = models.ImageField(upload_to='uploads/cars/', null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.car


class Cab(models.Model):
    driver_name = models.CharField(max_length=50)
    driver_contact_no = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$')])
    car_type = models.ForeignKey(CarType, null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Profile(models.Model):
    adress = models.CharField(max_length=150, null=True, blank=True)
    profile_pic = models.ImageField(upload_to='uploads/cars/', null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)

