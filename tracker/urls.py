from django.urls import path
from .views import dashboard,add_expense

urlpatterns = [
    path('', dashboard, name='dashboard'), 
    path('add-expense/', add_expense, name='add_expense'),

]
