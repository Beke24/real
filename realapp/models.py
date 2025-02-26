from django.db import models

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    email = models.EmailField(unique=True)
    profile_picture=models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.username 

# Create your models here.
class atendance(models.Model):
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)
    
    
    
    def __str__(self):
        return f"{self.user.username}{self.date}"
    
    
class task(models.Model):
        title=models.CharField(max_length=100)
        user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
        discripton=models.TextField(blank=True,null=True)
        
        
        def __str__(self):
            return f"{self.title}{self.user.username}"
    
