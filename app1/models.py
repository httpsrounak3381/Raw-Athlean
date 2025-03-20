from django.db import models

# Create your models here.
class RegTable(models.Model):
    fname=models.CharField(max_length=50,null=True)
    lname=models.CharField(max_length=50,null=True)
    DOB=models.DateField(null=True)
    gen=models.CharField(max_length=50,null=True)
    Age=models.IntegerField(null=True)
    Email=models.EmailField(max_length=70,null=True)
    Pass=models.IntegerField(null=True)
    mytext=models.CharField(max_length=200,null=True)
def __self__(self):
    return self.fname1

class RegTable2(models.Model):
    fname=models.CharField(max_length=50,null=True)
    lname=models.CharField(max_length=50,null=True)
    DOB=models.DateField(null=True)
    gen=models.CharField(max_length=50,null=True)
    Age=models.IntegerField(null=True)
    Email=models.EmailField(max_length=70,null=True)
    Pass=models.IntegerField(null=True)
    mytext=models.CharField(max_length=200,null=True)
def __self__(self):
    return self.fname1

class RegTable3(models.Model):
    fname=models.CharField(max_length=50,null=True)
    lname=models.CharField(max_length=50,null=True)
    DOB=models.DateField(null=True)
    gen=models.CharField(max_length=50,null=True)
    Payment_Method=models.CharField(max_length=50,null=True)
    PayMethod=models.CharField(max_length=50,null=True)
def __self__(self):
    return self.fname1