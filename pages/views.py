
from itertools import product
from django.shortcuts import render
from pages.models import Product

# Create your views here.


def index(request):
  
    return render(request, 'pages/index.html',{'pro':Product.objects.all()})

    

       


    






