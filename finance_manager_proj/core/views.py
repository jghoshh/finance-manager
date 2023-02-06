from django.views import View 
from django.shortcuts import render
from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.cache import cache_control
from django.utils.decorators import method_decorator
from .models import Expense
from datetime import datetime

# Create your views here.
categories = ["Groceries", "Eating Out", "Travel", "Rent", "Other"]

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def index(request): 
    if (not request.user.is_authenticated): 
        return HttpResponseRedirect(reverse('authentication:login'))

    expenses = Expense.objects.filter(owner=request.user)

    return render(request, 'finance_manager/index.html', {
        "title": "Your Expenses",
        "buttonName": "Add Expenses",
        "expenses": expenses
    } )

def redirectToHome(request): 
    return HttpResponseRedirect(reverse('core:index'))

class AddExp(View): 
    def get(self, request): 
        if (not request.user.is_authenticated): 
            return HttpResponseRedirect(reverse('authentication:login'))
        return render(request, 'finance_manager/add.html', {
        "title": "Add Expenses",
        "buttonName": "Go Back",
        "categories": categories,
        })
    
    def post(self, request): 
        if (not request.user.is_authenticated): 
            return HttpResponseRedirect(reverse('authentication:login'))

        amount = request.POST["amount"]
        description = request.POST["description"]
        date = request.POST["date"]
        category = request.POST["category"]

        if amount and date and category:
            if not description: 
                description = ""
            
            expense = Expense.objects.create(owner=request.user, amount=amount, date=date, description=description, typeOfExpense=category)
            expense.save()
            
            return render(request, 'finance_manager/add.html', {
            "title": "Add Expenses",
            "buttonName": "Go Back",
            "categories": categories,
            "successMessage": "Success! You have created an expense."})
        
        return render(request, 'finance_manager/add.html', {
        "title": "Add Expenses",
        "buttonName": "Go Back",
        "categories": categories,
        "errorMessage": "Amount, Date, and Category are all mandatory fields."
        })

class EditExp(View): 
    def get(self, request, expenseId): 

        if (not request.user.is_authenticated): 
            return HttpResponseRedirect(reverse('authentication:login'))

        expense = Expense.objects.get(id=expenseId)
        date = str(expense.date)
        description = str(expense.description)

        return render(request, 'finance_manager/edit.html', {
            "title": "Edit Expense",
            "expenseId": expenseId,
            "expense": Expense.objects.get(id=expenseId),
            "expenseDate": date,
            "expenseDescription": description,
            "buttonName": "Go Back",
            "categories": categories,
        })

    def post(self, request): 
        if (not request.user.is_authenticated): 
            return HttpResponseRedirect(reverse('authentication:login'))
        


        
