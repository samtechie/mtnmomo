from django.db import models
from django.conf import settings


# Create your models here.
class MomoRequest(models.Model):
    request_type = models.CharField(max_length=100,default="")
    request_status = models.CharField(max_length=100,default="")



