# Generated by Django 4.1.5 on 2023-02-06 09:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('cat_id', models.AutoField(primary_key=True, serialize=False)),
                ('cat_name', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('p_ip', models.CharField(max_length=200)),
                ('k_ip', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('p_id', models.AutoField(primary_key=True, serialize=False)),
                ('p_name', models.CharField(max_length=200)),
                ('p_price', models.IntegerField()),
                ('p_belong', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bill.users', verbose_name='User')),
                ('p_cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bill.category', verbose_name='Cat')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='cat_belong',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bill.users', verbose_name='User'),
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('cart_number', models.AutoField(primary_key=True, serialize=False)),
                ('cart_bp', models.CharField(max_length=100)),
                ('cart_data', models.TextField()),
                ('cart_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bill.users', verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_number', models.IntegerField()),
                ('bill_date', models.DateTimeField(auto_now_add=True)),
                ('bill_data', models.TextField()),
                ('bill_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bill.users', verbose_name='User')),
            ],
        ),
    ]
