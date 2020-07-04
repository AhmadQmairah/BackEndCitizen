from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Issue(models.Model):
    description = models.CharField(max_length=300)
    name = models.CharField(max_length=300,)
    phone_number = models.CharField(max_length=12)
    image = TextField()
    lat = models.DecimalField(max_digits=5, decimal_places=2)
    lng = models.DecimalField(max_digits=5, decimal_places=2)
    created_date = models.DateTimeField(auto_now_add=True)
