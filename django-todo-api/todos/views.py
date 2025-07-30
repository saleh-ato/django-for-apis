from rest_framework import generics
from .models import Todo
from .serializers import TodoSerializer
# from django.shortcuts import render

class ListTodo(generics.ListAPIView):
    queryset=Todo.objects.all()
    serializer_class=TodoSerializer

class DetailTodo(generics.RetrieveAPIView):
    queryset=Todo.objects.all()
    serializer_class=TodoSerializer