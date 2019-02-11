from django.shortcuts import render
from django.http import HttpResponse

from .models import Customer

# Create your views here.
def index(request):
    customers = Customer.objects.all()

    context = { 
        'title': 'Customers',
        'customers': customers
    }

    return render(request, 'customer/index.html', context)
