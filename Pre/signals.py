from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Image
import os


@receiver(post_delete, sender=Image)
def delete_image_file(sender, instance, **kwargs):
    if instance.image:
        storage, path = instance.image.storage, instance.image.path
        if os.path.isfile(path):
            storage.delete(path)
