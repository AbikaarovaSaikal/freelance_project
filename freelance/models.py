from django.db import models

# Create your models here.

class Job(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    payment = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    update_at = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return f"{self.name}"