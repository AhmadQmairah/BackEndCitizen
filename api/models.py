from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Issue(models.Model):
    description = models.CharField(max_length=300)
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="issues")
    image = ImageField(upload_to=None)
    lat = models.DecimalField(max_digits=5, decimal_places=2)
    lng = models.DecimalField(max_digits=5, decimal_places=2)
    created_date = models.DateTimeField(auto_now_add=True)
