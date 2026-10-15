from django.db import models

# Create your models here.
from django.db import models
class Employee(models.Model):
    gender_choices=(('male','MALE'),('female','FEMALE'))
    empid=models.IntegerField()
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    gender=models.CharField(choices=gender_choices,max_length=10)
    salary=models.IntegerField()
    designation=models.CharField(max_length=50,)
    join_date=models.DateField(auto_now_add=True)
    # Create your models here.
