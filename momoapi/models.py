from django.db import models


# Create your models here.
class MomoRequest(models.Model):
    request_type = models.CharField(max_length=100,default="")
    request_status = models.CharField(max_length=100,default="")



