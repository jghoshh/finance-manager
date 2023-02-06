from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

class Expense(models.Model): 
    id = models.AutoField(primary_key=True)
    amount = models.FloatField()
    date = models.DateField(default=now)
    description = models.TextField()
    owner=models.ForeignKey(to=User, on_delete=models.CASCADE)
    typeOfExpense=models.CharField(max_length=256)

    class Meta:
        # order the  returned expenses by most recent to least when querying it.
        ordering = ['-date']

    def __repr__(self):
        return f"Expense: amt: {self.amount}, date: {self.date}, owner: {self.owner}"


