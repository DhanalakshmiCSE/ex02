from django.db import models
from django.contrib import admin
# Create your models here.
class Employee (models.Model):
    EMP_ID=models.CharField(max_length=20,help_text='EMP_ID')
    ENAME=models.CharField(max_length=100)
    POST=models.CharField(max_length=100)
    SALARY=models.IntegerField()
    AGE=models.IntegerField()

class EmployeeAdmin(admin.ModelAdmin):
    list_display=('EMP_ID','ENAME','POST','SALARY','AGE')

