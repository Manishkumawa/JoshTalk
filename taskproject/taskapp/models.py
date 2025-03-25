from django.db import models

# Create your models here.

from django.db import models


from django.contrib.auth.models import AbstractUser,User
from django.core.validators import RegexValidator

class User(AbstractUser):
    mobile = models.CharField(
        max_length=15,
        blank=True,
        null=True    
    )
    email = models.EmailField(unique=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    def __str__(self):
        return self.email





class Task(models.Model):
    TASK_TYPES = (
        ('personal', 'Personal'),
        ('work', 'Work'),
        ('shopping', 'Shopping'),
        ('other', 'Other'),
    )
    
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    )
    
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    task_type = models.CharField(max_length=20, choices=TASK_TYPES, default='personal')
    completed_at = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    assigned_users = models.ManyToManyField(User, related_name='tasks')
    
    def __str__(self):
        return self.name

