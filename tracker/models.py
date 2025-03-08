from django.db import models

class Expense(models.Model):
    date = models.DateField()  # Stores the date of the expense
    category = models.CharField(max_length=50)  # Stores the category (Food, Travel, etc.)
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Stores the amount spent

    def __str__(self):
        return f"{self.category} - ₹{self.amount} on {self.date}"
