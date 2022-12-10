from django.db import models
from datetime import date
# Todo
class Task(models.Model):

    # Choices for status field
    status_choices = [
        ("OPEN", "Open"), 
        ("WORKING", "Working"), 
        ("DONE", "Done"), 
        ("OVERDUE", "Overdue"), 
    ]

    timestamp = models.DateTimeField(auto_now_add=True, editable=False)
    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.CharField(max_length=1000, blank=False, null=False)
    due_date = models.DateField(default= date.today)
    tag = models.CharField(max_length=100)
    status = models.CharField(max_length=10, choices=status_choices, default="OPEN", null=False)

    def __str__(self):
        return self.title