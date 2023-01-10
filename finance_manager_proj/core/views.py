from django.shortcuts import render

# Create your views here.
def index(request): 
    return render(request, 'finance_manager/index.html')

def add_exp(request): 
    return render(request, 'finance_manager/add.html') 

