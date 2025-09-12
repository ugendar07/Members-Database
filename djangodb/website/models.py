from django.db import models

class Member(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    age = models.IntegerField(3)
    email = models.EmailField(max_length=100)
    passwd = models.CharField(max_length=50)


    def __str__(self):
        return self.fname + ' ' + self.lname
        
