from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

# Create your views here.
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Task, User
from .serializers import TaskSerializer, TaskCreateSerializer,TaskAssignSerializer, UserSerializer,UserCreateSerializer

class TaskCreateView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskCreateSerializer
    
    def perform_create(self, serializer):
        serializer.save()

class TaskAssignView(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskAssignSerializer
    
    def update(self, request, *args, **kwargs):
        task = self.get_object()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        user_ids = serializer.validated_data['user_ids']
        users = User.objects.filter(id__in=user_ids)
        task.assigned_users.add(*users)
        
        return Response({'status': 'users assigned successfully'})

class UserTasksView(generics.ListAPIView):
    serializer_class = TaskSerializer
    
    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Task.objects.filter(assigned_users__id=user_id)

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    
    
    def perform_create(self, serializer):
        instance = serializer.save()
        instance.set_password(instance.password)
        instance.save()