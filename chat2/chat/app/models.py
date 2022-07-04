from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class room(models.Model):
    name = models.CharField(max_length=50,unique=True)
    
    def __str__(self):
        return self.name
    
class message(models.Model):
    room = models.ForeignKey(room,on_delete=models.CASCADE)
    name = models.CharField(max_length=1000)
    msg = models.TextField(null=True,blank=True)
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('date',)
        
    def __str__(self):
        return self.name
    
    

    