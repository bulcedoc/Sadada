# Generated by Django 4.1.5 on 2023-02-07 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0002_alter_users_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='cart_data',
            field=models.IntegerField(),
        ),
    ]
