from django.shortcuts import render
from django.http import HttpResponse
from .models import Bill, Clint, Employee


def index(request):
    return render(request, 'bill/index.html')


def add(request):
    if request.method == 'POST':
        customer = request.POST.get('customer')
        phone = request.POST.get('phoneno')
        pieces = request.POST.get('pieces')
        pmoney = request.POST.get('pmoney')
        umoney = request.POST.get('umoney')
        tmoney = request.POST.get('tmoney')
        addbill = Bill(bill_clint_name=customer, bill_product_pcs=pieces,
                       total_price=tmoney, bill_paid=pmoney, bill_unpaid=umoney, bill_mobile_number=phone)
        addbill.save()
        return HttpResponse('Bill Added')
    return render(request, 'bill/add.html')


def allbills(request):
    if request.method == 'POST':
        mydelete = request.POST.get('delid')
        instance = Bill.objects.get(bill_id=mydelete)
        instance.delete()
        bills = Bill.objects.all()
        parmas = {'data': bills}
        return render(request, 'bill/allbills.html', parmas)
    else:
        bills = Bill.objects.all()
        parmas = {'data': bills}
        return render(request, 'bill/allbills.html', parmas)


def employee(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        addr = request.POST.get('addr')
        pnum = request.POST.get('pnum')
        addemployee = Employee(employee_name=name, employee_address=addr,
                               employee_number=pnum)
        addemployee.save()
        return HttpResponse('Employee Added')
    return render(request, 'bill/employee.html')
