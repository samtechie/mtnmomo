from django.db import models
from django.conf import settings

from mtnmomo.collection import Collection
client = Collection({
    "COLLECTION_USER_ID": settings.COLLECTION_USER_ID,
    "COLLECTION_API_SECRET": settings.COLLECTION_API_SECRET,
    "COLLECTION_PRIMARY_KEY": settings.COLLECTION_PRIMARY_KEY,
})


# Create your models here.
class MomoRequestManager(models.Manager):
    def create_request(self,request_type):
        request =self.create(request_type=request_type)
         client.requestToPay(
           mobile="256772123456", amount="600", external_id="123456789", payee_note="dd", payer_message="dd", currency="EUR")

class MomoRequest(models.Model):
    request_type = models.CharField(max_length=100)
    request_status = models.CharField(max_length=100)

