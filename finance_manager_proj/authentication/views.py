import json
import re
from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib import auth
from django.urls import reverse
from django.views.decorators.cache import cache_control
from django.utils.decorators import method_decorator

# Create your views here.
# Since the registration path can be POSTED to and GOTTEN, we will use a class based view to simplify the check of type of request.
class RegistrationView(View): 
    def get(self, request): 
        if (request.user.is_authenticated): 
           return HttpResponseRedirect(reverse('core:index'))
        return render(request, 'authentication/register.html')
    
    def post(self, request): 
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not User.objects.filter(email=email).exists() and not User.objects.filter(username=username).exists(): 
            user = User.objects.create_user(username=username, email=email)
            user.set_password(password)
            user.save()
            return render(request, 'authentication/login.html', context={"successRegister": True})
        return render(request, 'authentication/register.html')



class LoginView(View): 
    
    @method_decorator(cache_control(no_cache=True, must_revalidate=True))
    def get(self, request):  
        if (request.user.is_authenticated): 
           return HttpResponseRedirect(reverse('core:index'))
        return render(request, 'authentication/login.html', context={"justGetting": True})
    
    def post(self, request): 
        email = request.POST.get('email')
        password = request.POST.get('password')

        if email and password: 
            user = User.objects.get(email=email)
            if user: 
                auth.authenticate(username=user.username, password=password)
                if user and user.is_active: 
                    auth.login(request, user)
                    return HttpResponseRedirect(reverse('core:index'))
            return render(request, 'authentication/login.html', context={"succesLogin": False})


class LogoutView(View): 

    def post(self, request): 
        auth.logout(request)
        return HttpResponseRedirect(reverse('authentication:login'))

    def get(self, request): 
        auth.logout(request)
        return HttpResponseRedirect(reverse('authentication:login'))
        
        
# We will create another view for username validation.
# No need for csrf token here, because this view is just a validator of some inputted value.
def username_validation(request): 
    if request.method == 'POST':
        data = json.loads(request.body)
        username = str(data['username'])

        if not username.isalnum(): 
            #making the response a 400 status code because it contains an invalid username.
            return JsonResponse({"username_error": "The username should only contain alphanumeric characters."},status=400)
        
        if User.objects.filter(username=username).exists(): 
            #making the response a 409 status code because it signifies that the resource is competing with another.
            return JsonResponse({'username_error': "The username is already in use."}, status=409)

        return JsonResponse({'is_username_valid': True})
    
    else:
        return HttpResponseNotAllowed(('POST',))

# We will create another view for username validation.
# No need for csrf token here, because this view is just a validator of some inputted value.
def email_validation(request): 
    if request.method == 'POST':
        data = json.loads(request.body)
        email= str(data['email'])
        mailFormat = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

        if not re.search(mailFormat, email): 
            return JsonResponse({"email_error": "Email is not valid."}, status=400)
        
        if User.objects.filter(email=email).exists(): 
            #making the response a 409 status code because it signifies that the resource is competing with another.
            return JsonResponse({'email_error': "The email is already in use."}, status=409)

        return JsonResponse({'is_email_valid': True})
    
    else:
        return HttpResponseNotAllowed(('POST',))

def password_validation(request): 
    if request.method == 'POST':
        data = json.loads(request.body)
        password = str(data['pass'])

        if len(password) < 8: 
            return JsonResponse({"pass_error": "Password must be at least 8 characters."}, status=400)

        return JsonResponse({'is_pass_valid': True})
    
    else:
        return HttpResponseNotAllowed(('POST',))




        



