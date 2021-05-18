# Generated by Django 3.1.6 on 2021-02-19 17:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Classification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_user', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DestinationType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='LifeStyleIndex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SurgePricingType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surge_price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CreateUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user_acc', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.classification')),
            ],
        ),
        migrations.CreateModel(
            name='CabPredictionModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trip_distance', models.FloatField(default=0)),
                ('cancellation_last_one_month', models.IntegerField()),
                ('customer_since_month', models.FloatField(default=0)),
                ('customer_rating', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.customerrating')),
                ('destination_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.destinationtype')),
                ('gender', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.gender')),
                ('life_style_index', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.lifestyleindex')),
                ('surge_pricing_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.surgepricingtype')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
