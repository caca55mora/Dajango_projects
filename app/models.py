from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    customer = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, null=True)
    address = models.CharField(max_length=100, null=True)
    image = models.ImageField(default='default.jpg', upload_to = 'Profile_Pic')

    class Meta:
        verbose_name_plural = 'Profile'


    def __str__(self):
        return f'{self.customer.username} profile'
    
class Appointment(models.Model):
    customer=models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=100,blank=True,null=True)
    email = models.EmailField(blank=True,null=True)
    service = models.CharField(max_length=50,null=True,blank=True)
    contact = models.CharField(max_length=100,blank=True,null=True)
    date = models.DateField(blank=True,null=True)
    time = models.CharField(max_length=10,blank=True,null=True)
    status = models.BooleanField(default=False)

    
    class Meta:
        verbose_name_plural = 'Appointments'

  
    def __str__(self):
        return self.name 

