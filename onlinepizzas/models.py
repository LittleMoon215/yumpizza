from pyexpat import model

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from yumpizza import settings


class Pizza(models.Model):
    name = models.CharField(max_length=60, unique=True)
    description = models.CharField(max_length=250)
    price = models.IntegerField(default=0, editable=True)
    mass = models.IntegerField()

    class Meta:
        db_table = "pizza"
        managed = True

    def __str__(self):
        return self.name


class Drink(models.Model):
    name = models.CharField(max_length=60, unique=True)
    description = models.CharField(max_length=250)
    price = models.IntegerField(default=0, editable=True)

    class Meta:
        db_table = "drink"
        managed = True

    def __str__(self):
        return self.name


class Snack(models.Model):
    name = models.CharField(max_length=60, unique=True)
    description = models.CharField(max_length=250)
    price = models.IntegerField(default=0, editable=True)

    class Meta:
        db_table = "snack"
        managed = True

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="member", on_delete=models.CASCADE)
    order_timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "order"
        managed = True

    def __str__(self):
        return str(self.pk)


class OrderPizza(models.Model):
    itemId = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    orderId = models.ForeignKey(Order, on_delete=models.CASCADE)
    Qty = models.IntegerField(default=1)

    def __str__(self):
        return str(self.orderId)


class OrderDrink(models.Model):
    itemId = models.ForeignKey(Drink, on_delete=models.CASCADE)
    orderId = models.ForeignKey(Order, on_delete=models.CASCADE)
    Qty = models.IntegerField(default=1)

    def __str__(self):
        return str(self.orderId)


class OrderSnack(models.Model):
    itemId = models.ForeignKey(Snack, on_delete=models.CASCADE)
    orderId = models.ForeignKey(Order, on_delete=models.CASCADE)
    Qty = models.IntegerField(default=1)

    def __str__(self):
        return str(self.orderId)


class UserManager(BaseUserManager):
    def create_user(self, number, email, first_name, last_name, birthday, password=None):
        if number is None:
            raise TypeError("Username cannot be blank")
        if email is None:
            raise TypeError("Email cannot be blank")
        user = self.model(number=number, email=self.normalize_email(email), first_name=first_name, last_name=last_name,
                          birthday=birthday)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, number, email, first_name, last_name, birthday, password):
        if password is None:
            raise TypeError("Enter password")
        user = self.create_user(number, email, first_name, last_name, birthday, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    number = models.CharField(db_index=True, max_length=12, unique=True)
    email = models.EmailField(db_index=True, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    birthday = models.DateField()
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    USERNAME_FIELD = 'number'
    REQUIRED_FIELDS = ['email', 'birthday', 'first_name', 'last_name']
    objects = UserManager()

    class Meta:
        managed = True
        db_table = "users"

    def __str__(self):
        return self.number


class Position(models.Model):
    title = models.CharField(db_index=True, unique=True, max_length=50)
    number_of_vacancy = models.IntegerField()
    payment = models.IntegerField()

    def __str__(self):
        return self.title


class Workers(models.Model):
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    birthday = models.DateField()
    employment_date = models.DateField()
    number = models.CharField(db_index=True, unique=True, max_length=12)
    employment_history_number = models.CharField(max_length=30)
    email = models.EmailField(db_index=True, unique=True)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

    def __str__(self):
        return self.number


class FeedBack(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)


class Product(models.Model):
    title = models.CharField(max_length=50, unique=True)
    amount = models.IntegerField()

    def __str__(self):
        return self.title


class Recipe(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.DO_NOTHING)
    ingredient = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    mass = models.IntegerField()

    def __str__(self):
        return self.pizza


class DecommissionedProduct(models.Model):
    amount = models.IntegerField()
    dateOfDecommission = models.DateField()
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.product


class Distributor(models.Model):
    phone = models.CharField(max_length=12, unique=True, db_index=True)
    email = models.TextField()
    productType = models.TextField()

    def __str__(self):
        return self.phone


class DistributorOrder(models.Model):
    price = models.IntegerField()
    estimatedDate = models.DateField()
    orderDate = models.DateField(auto_now_add=True)
    orderStatus = models.CharField(max_length=50)
    lastDeliveryDate = models.DateField()
    distributor = models.ForeignKey(Distributor, on_delete=models.DO_NOTHING)
    orderContent = models.TextField()

    def __str__(self):
        return self.orderDate
