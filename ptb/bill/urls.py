from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='HomeBill'),
    path('add', views.add, name='AddInvoice'),
    path('allbills', views.allbills, name="AllBills"),
    path('addemployee', views.employee, name="AddEmployee")
]
