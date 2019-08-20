from django.db.models.signals import pre_save
from django.dispatch import receiver
from momoapi.models import MomoRequest
from mtnmomo.collection import Collection
from django.conf import settings


client = Collection({
    "COLLECTION_USER_ID": settings.COLLECTION_USER_ID,
    "COLLECTION_API_SECRET": settings.COLLECTION_API_SECRET,
    "COLLECTION_PRIMARY_KEY": settings.COLLECTION_PRIMARY_KEY,
})


@receiver(pre_save, sender=MomoRequest)
def create_request(sender, instance, **kwargs):
    request = client.requestToPay(
           mobile="256775141771", amount="600", external_id="123456789", payee_note="dd", payer_message="dd", currency="EUR")
    return client.getTransactionStatus(request["transaction_ref"])
