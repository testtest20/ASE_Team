from django.shortcuts import render
from .models import *
from .forms import medicineform
# Create your views here.

def orderpage(request):
    search=medicines.objects.all()
    name=None
    if 'search' in request.GET:
       name=request.GET['search']
       if name: 
          search=search.filter(name__icontains=name) 

    context={
       'cat':category.objects.all(),
        'med':search,
        'form':medicineform(),
        'allmedicines':medicines.objects.filter(active=True).count(),
        'medavailable':medicines.objects.filter(status='available').count(),
        'medunavailable':medicines.objects.filter(status='unavailable').count(),
    }
    return render(request,'pages/orderpage.html',context)

def orderpage2(request):
    context={
        'med':medicines.objects.all(),
        'form':medicineform(),
        'allmedicines':medicines.objects.filter(active=True).count(),
        'medavailable':medicines.objects.filter(status='available').count(),
        'medunavailable':medicines.objects.filter(status='unavailable').count(),
    }
    return render(request,'pages/orderpage2.html',context)








