# Generated by Django 4.1.5 on 2023-02-07 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0003_alter_cart_cart_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='cart_name',
            field=models.CharField(default=2, max_length=100),
            preserve_default=False,
        ),
    ]