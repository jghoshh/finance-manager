from django.shortcuts import render
from django.views import View

# Create your views here.
# Since the registration path can be POSTED to and GOTTEN, we will use a class based view to simplify the check of type of request.
class RegistrationView(View): 
    def get(self, request): 
        return render(request, 'authentication/register.html')