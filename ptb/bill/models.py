from django.db import models
from datetime import date
from django.utils import timezone


class Clint(models.Model):
    clint_id = models.AutoField(primary_key=True)
    clint_name = models.CharField(max_length=250)
    clint_piece = models.IntegerField()
    clint_pmoney = models.IntegerField()
    clint_umoney = models.IntegerField()

    def __str__(self):
        return self.clint_name


class Bill(models.Model):
    bill_id = models.AutoField(primary_key=True)
    bill_date = models.DateField(auto_now_add=True)
    bill_clint_name = models.CharField(max_length=250)
    bill_product_pcs = models.IntegerField(default=0)
    total_price = models.IntegerField(default=0)
    bill_paid = models.IntegerField(default=0)
    bill_unpaid = models.IntegerField(default=0)
    bill_mobile_number = models.CharField(max_length=10)

    def __str__(self):
        return self.bill_clint_name + " @ " + str(self.bill_date)


class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_name = models.CharField(max_length=250)
    employee_address = models.CharField(max_length=250)
    employee_number = models.CharField(max_length=10)

    def __str__(self):
        return self.employee_name
