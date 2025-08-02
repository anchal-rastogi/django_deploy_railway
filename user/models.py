from django.db import models

# Create your models here.
class tblcontact(models.Model):
    name=models.CharField(max_length=50,null=True)
    email=models.EmailField(max_length=50,null=True)
    mobile=models.CharField(max_length=20,null=True)
    message=models.TextField(null=True)