# Generated by Django 4.1.4 on 2023-03-08 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0006_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
    ]
