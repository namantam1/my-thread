from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Thread(models.Model):
    thread = models.CharField(max_length=25)
    timestamp = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    text = models.TextField()
    name = models.CharField(max_length=225)
    email = models.EmailField()
    created_on = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.name}"
    
