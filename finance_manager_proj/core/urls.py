from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('add-exp', views.AddExp.as_view(), name='add'),
    path('edit-exp/<int:expenseId>', views.EditExp.as_view(), name='edit'),
    path('edit-exp/', views.redirectToHome, name='redirectToHomeFromEdit')
]
