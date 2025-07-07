from django.db import models

# Create your models here.

class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    about = models.TextField()
    types= models.CharField(max_length=100,choices=(('IT','IT'),
                                                    ('Non IT','Non IT'),
                                                    ('Mobile Phones','Mobile Phones')
                                                    ))
    added_time =models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    
    
    def __str__(self):
        return self.name +' -- '+ self.location
    
    
    
class Employee(models.Model):
    name = models.CharField(max_length=50)
    email =models.EmailField(unique=True)
    address = models.CharField(max_length=100)
    phone = models.IntegerField(default=0,null=True)
    about = models.TextField()
    position = models.CharField(max_length=50,choices=(('Manager','Manager'),
                                                       ('Software Developer','SD'),
                                                       ('Project Leader','PL')
                                                       ))
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.name