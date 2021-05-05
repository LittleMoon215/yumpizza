from pyexpat import model

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from yumpizza import settings


class Pizza(models.Model):
    name = models.CharField(max_length=60, unique=True)
    description = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=4, decimal_places=2, default=0.00, editable=False)

    class Meta:
        db_table = "pizza"
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


class OrderDetails(models.Model):
    orderId = models.ForeignKey(Order, on_delete=models.CASCADE)
    itemId = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    Qty = models.IntegerField(default=1)

    class Meta:
        managed = True
        db_table = "order_details"

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
