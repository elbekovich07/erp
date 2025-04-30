from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Video

@receiver(post_save, sender=Video)
def update_status_to_ready(sender, instance, created, **kwargs):
    if created:
        instance.status = Video.StatusChoice.READY
        instance.save()
