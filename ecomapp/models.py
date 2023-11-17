from django.db import models

# Create your models here.

class register(models.Model):
    fname=models.CharField(max_length=30)
    lname=models.CharField(max_length=20)
    username=models.CharField(max_length=20)
    email=models.EmailField()
    phone=models.IntegerField()
    gender=models.CharField(max_length=20)
    dob=models.DateField()
    address = models.CharField(max_length=100)
    detaddress=models.CharField(max_length=100)
    password=models.CharField(max_length=20)
    fiimg = models.FileField(upload_to='ecomapp/static')
    def __str__(self):
        return self.fname


















class login(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=20)



class upload(models.Model):
    pname=models.CharField(max_length=20)
    fileimage=models.FileField(upload_to='ecomapp/static')
    pdes=models.CharField(max_length=200)
    price=models.IntegerField(max_length=30)