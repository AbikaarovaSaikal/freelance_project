from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    update_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f"{self.name}"

class Job(models.Model):
    photo = models.ImageField(blank=True, null=True, upload_to='freelance/')
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    payment = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    update_at = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return f"{self.name}"