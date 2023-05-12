# Generated by Django 4.1.4 on 2023-02-20 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.BigIntegerField()),
                ('password', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'admin',
            },
        ),
    ]
