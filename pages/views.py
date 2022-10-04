
from distutils.command.build_scripts import first_line_re
from itertools import product
from re import X
import re
from urllib.request import Request
from django.shortcuts import render
from pages.models import Product

# Create your views here.


def index(request):
  
    return render(request, 'pages/index.html',{'pro':Product.objects.all()})






def form(request):
    if request.method == 'POST':    
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        Dept_name = request.POST.get('Dept_name')
        joining_date = request.POST.get('joining_date')
        Price = request.POST.get('Price')
        image = request.POST.get('image')
        
        

        


        data = Product(first_name=first_name,last_name=last_name,Dept_name=Dept_name,joining_date=joining_date,Price=Price,image= image)
        data.save()
    
    return render(request, 'pages/form.html')









    

       


    






