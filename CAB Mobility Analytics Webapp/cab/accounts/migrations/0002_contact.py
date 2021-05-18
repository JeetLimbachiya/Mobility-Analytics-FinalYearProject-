# Generated by Django 3.1.6 on 2021-02-25 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('email', models.CharField(max_length=100, null=True)),
                ('subject', models.CharField(max_length=500, null=True)),
                ('message', models.CharField(max_length=500, null=True)),
            ],
        ),
    ]
