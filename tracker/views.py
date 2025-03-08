from django.shortcuts import render, redirect
from django.utils.timezone import now
from .models import Expense

def dashboard(request):
    expenses = Expense.objects.all().order_by('-date')[:5]  # Show last 5 expenses
    return render(request, 'tracker/dashboard.html', {'expenses': expenses})

def add_expense(request):
    if request.method == 'POST':
        date = request.POST.get('date', now().date())
        category = request.POST.get('category', 'Others')
        amount = request.POST.get('amount')

        Expense.objects.create(date=date, category=category, amount=amount)
        return redirect('dashboard')

    return redirect('dashboard')
