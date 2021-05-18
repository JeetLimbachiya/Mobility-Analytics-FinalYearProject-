from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils.timezone import now


class Classification(models.Model):
    account_user = models.CharField(max_length=50)

    def __str__(self):
        return str(self.account_user)


class CreateUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_acc = models.ForeignKey(Classification, null=True, on_delete=models.SET_NULL)
    date = models.DateField(default=now)

    def __str__(self):
        return str(self.user)


class LifeStyleIndex(models.Model):
    index = models.IntegerField()

    def __str__(self):
        return str(self.index)


class DestinationType(models.Model):
    destination = models.IntegerField()

    def __str__(self):
        return str(self.destination)


class CustomerRating(models.Model):
    rating = models.IntegerField()

    def __str__(self):
        return str(self.rating)


class Gender(models.Model):
    gender = models.IntegerField()

    def __str__(self):
        return str(self.gender)


class SurgePricingType(models.Model):
    surge_price = models.IntegerField()

    def __str__(self):
        return str(self.surge_price)


class CabPredictionModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    trip_distance = models.FloatField(default=0)
    life_style_index = models.ForeignKey(LifeStyleIndex, null=True, on_delete=models.SET_NULL)
    destination_type = models.ForeignKey(DestinationType, null=True, on_delete=models.SET_NULL)
    customer_rating = models.ForeignKey(CustomerRating, null=True, on_delete=models.SET_NULL)
    gender = models.ForeignKey(Gender, null=True, on_delete=models.SET_NULL)
    surge_pricing_type = models.ForeignKey(SurgePricingType, null=True, on_delete=models.SET_NULL)
    cancellation_last_one_month = models.IntegerField()
    customer_since_month = models.FloatField(default=0)

class Contact(models.Model):
    name = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    subject = models.CharField(max_length=500, null=True)
    message = models.CharField(max_length=500, null=True)


    # def get_date(self):
    #     date = CreateUser.objects.get
    #     if self.created_at.year == today.year:
    #         created_at = str(today.month - self.created_at.month)
    #     return self.created_at

    





