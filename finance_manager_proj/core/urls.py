from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('add-exp', views.AddExp.as_view(), name='add'),
    path('edit-exp/<int:expenseId>', views.EditExp.as_view(), name='edit'),
    path('edit-exp/', views.redirectToHome, name='redirectToHomeFromEdit'),
    path('delete-exp/<int:expenseId>', views.deleteExp, name='delete'),
    # right now anyone can access this endpoint, but in the future, we would want only devs or 
    # those authorized to access this endpoint. We could use token auth for that.
    path('dev-expense-summary/<str:date>', views.getExpenseSummary, name='getExpenseSummary'),
    path('expense-summary/<str:date>', views.expenseSummary, name='expenseSummary')
]
