from django.contrib import admin
from .models import Bill, Employee, Clint

admin.site.register(Clint)
admin.site.register(Bill)
admin.site.register(Employee)
