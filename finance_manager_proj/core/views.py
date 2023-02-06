from django.views import View 
from django.shortcuts import render
from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.cache import cache_control
from django.utils.decorators import method_decorator
from .models import Expense
from datetime import datetime
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.
categories = ["Groceries", "Eating Out", "Transportation", "Rent", "Utilities", "Entertainment", "Other"]

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def index(request): 
    if (not request.user.is_authenticated): 
        return HttpResponseRedirect(reverse('authentication:login'))

    expenses = Expense.objects.filter(owner=request.user)
    paginator = Paginator(expenses, 4)
    page_number = request.GET.get('page')
    page_obj = Paginator.get_page(paginator, page_number)


    return render(request, 'finance_manager/index.html', {
        "title": "Your Expenses",
        "buttonName": "Add Expenses",
        "page_obj": page_obj,
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

    def post(self, request, expenseId): 
        if (not request.user.is_authenticated): 
            return HttpResponseRedirect(reverse('authentication:login'))
        
        expense = Expense.objects.get(id=expenseId)
        amount = request.POST["amount"]
        description = request.POST["description"]
        date = request.POST["date"]
        category = request.POST.get("category", None)

        if expense and amount and date: 
                expense.amount = amount
                expense.date = date
                if category: expense.typeOfExpense = category
                if description: expense.description = description
                expense.save()

        messages.success(request, "Success! You have edited the expense.")
        return HttpResponseRedirect(reverse("core:index"))

def deleteExp(request, expenseId): 
    print(request.META.get('HTTP_REFERER', None))
    if (request.META.get('HTTP_REFERER', None) and request.META['HTTP_REFERER'][-2:-11:-1] == "/pxe-tide"):
        try: 
            expenseToDelete = Expense.objects.get(pk=expenseId, owner=request.user)
            expenseToDelete.delete()
            messages.success(request, "Success! You have deleted the expense")
            return HttpResponseRedirect(reverse("core:index"))

        except: 
            return HttpResponseRedirect(request.META.get['HTTP_REFERER'])

    return HttpResponseRedirect(reverse("core:index"))

            
        


        
