#from django.contrib.auth.models import AbstractUser
from django.db import models

#from django.contrib.auth.models import User

# Create your models here.


class sathiya(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField(null=True,blank=True)
    
# admin page
 
 
#class Post(models.Model):
 #  title=models.CharField(max_length=100)
  # content = models.TextField()
   #author=models.ForeignKey(User,on_delete=models.CASCADE)
   #created_at= models.DateTimeField(auto_now_add=True)
   #def __str__(self):
     #  return self.title
#class Item(models.Model):
 #      name=models.CharField(max_length=100)
  #     description = models.TextField()
   #    price = models.DecimalField(max_digits=10, decimal_places=2)
    #   def __str__(self) :
      #     return self.name
       


#class CustomUser(AbstractUser):
 #   # Add any custom fields if needed
  #  pass
