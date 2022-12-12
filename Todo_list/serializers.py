from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id','timestamp', 'title', 'description', 'due_date', 'tag', 'status')
