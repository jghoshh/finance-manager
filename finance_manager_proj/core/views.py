from django.shortcuts import render
from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib import auth
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.utils.decorators import method_decorator

# Create your views here.
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def index(request): 
    if (not request.user.is_authenticated): 
        return HttpResponseRedirect(reverse('authentication:login'))
    return render(request, 'finance_manager/index.html')

def add_exp(request): 
    return render(request, 'finance_manager/add.html') 

