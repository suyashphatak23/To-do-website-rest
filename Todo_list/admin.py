from django.contrib import admin
from .models import Task

# Admin View
class TaskAdmin(admin.ModelAdmin):
    list_display = ['record_date','record_time', 'title', 'description', 'due_date', 'tag', 'status']


admin.site.register(Task, TaskAdmin)