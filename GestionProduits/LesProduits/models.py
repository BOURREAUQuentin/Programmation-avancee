from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(auto_now=True)
    schedule_date = models.DateTimeField(auto_now=True)
    closed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name + ": " + self.description