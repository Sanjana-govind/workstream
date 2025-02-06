
from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    STATUS_CHOICES = [
        ('todo', 'To-Do'),
        ('pre_inprogress', 'Pre-Processing (In Progress)'),
        ('pre_done', 'Pre-Processing (Done)'),
        ('dev_inprogress', 'Development (In Progress)'),
        ('dev_done', 'Development (Done)'),
        ('done', 'Done'),
        ('urgent', 'Urgent Action Required'),
    ]

    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='todo')
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class UrgentTask(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ActivityLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=255)  # Stores action text
    timestamp = models.DateTimeField(auto_now_add=True)  # Auto timestamp

    def __str__(self):
        return f"{self.user.username} - {self.action} - {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}"



from django.db import models
from django.contrib.auth.models import User

class ArchivedTask(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    completed_at = models.DateTimeField(auto_now_add=True)  # Store deletion timestamp
    deleted_by = models.ForeignKey(User, on_delete=models.CASCADE)  # Track user who deleted the task

    def __str__(self):
        return f"{self.title} (Completed on {self.completed_at})"

























