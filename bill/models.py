from django.db import models

class Users(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100, unique=True)
    p_ip = models.CharField(max_length=200)
    k_ip = models.CharField(max_length=200)
    def __str__(self):
        return self.username
class Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    cat_name = models.CharField(max_length=200,unique=True)
    cat_belong = models.ForeignKey(Users,verbose_name="User", on_delete=models.CASCADE)
    def __str__(self):
        return self.cat_name
class Products(models.Model):
    p_id = models.AutoField(primary_key=True)
    p_name = models.CharField(max_length=200)
    p_price = models.IntegerField()
    p_cat = models.ForeignKey(Category,verbose_name="Cat", on_delete=models.CASCADE)
    p_belong = models.ForeignKey(Users,verbose_name="User", on_delete=models.CASCADE)
    def __str__(self):
        return self.p_name
class Bill(models.Model):
    bill_number = models.IntegerField()
    bill_user = models.ForeignKey(Users,verbose_name="User", on_delete=models.CASCADE)
    bill_date = models.CharField(max_length=100)
    bill_data = models.CharField(max_length=100)
    bill_amount = models.IntegerField()
    bill_pay = models.CharField(max_length=100)
    def __str__(self):
        return self.bill_number
class Cart(models.Model):
    cart_number =  models.AutoField(primary_key=True)
    cart_name = models.CharField(max_length=100)
    cart_user = models.ForeignKey(Users,verbose_name="User", on_delete=models.CASCADE)
    cart_bp = models.CharField(max_length=100)
    cart_data = models.IntegerField()
    cart_live = models.BooleanField()
    def __str__(self):
        return self.cart_number