# Generated by Django 4.1.5 on 2023-02-07 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0005_cart_cart_live'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bill',
            name='bill_data',
        ),
        migrations.AddField(
            model_name='bill',
            name='bill_pay',
            field=models.CharField(default=12, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bill',
            name='bill_pro',
            field=models.CharField(default=12, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bill',
            name='bill_quan',
            field=models.IntegerField(default=12),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bill',
            name='bill_date',
            field=models.CharField(max_length=100),
        ),
    ]