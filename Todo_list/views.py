from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer

#  view
class TodoViewset(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer