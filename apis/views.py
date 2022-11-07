from rest_framework import generics

from todos import models
from .serializers import TodoSerializer

from rest_framework import viewsets




class TodoViewSet(viewsets.ModelViewSet):
    queryset = models.Todo.objects.all()
    serializer_class = TodoSerializer


# class ListTodo(generics.ListCreateAPIView):
#     queryset = models.Todo.objects.all()
#     serializer_class = TodoSerializer


# class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
#     queryset = models.Todo.objects.all()
#     serializer_class = TodoSerializer
