from django.db import models

class Signup(models.Model):
    name = models.CharField(max_length=50)
    ussername = models.CharField(max_length=50)
    password = models.CharField(max_length=70, default="")
    phone = models.IntegerField(max_length=70, default="")


    def __str__(self):
        return self.name
    