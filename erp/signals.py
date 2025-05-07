from django.core.cache import cache
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Video, Course


@receiver(post_save, sender=Video)
def update_status_to_ready(sender, instance, created, **kwargs):
    if created:
        instance.status = Video.StatusChoice.READY
        instance.save()


@receiver([post_save, post_delete], sender=Course)
def clear_course_cache(sender, instance, **kwargs):
    print(">>> CACHE CLEARED")

    for page in range(1, 10000):
        cache.delete(f'courses_page_{page}_cat_')
        cache.delete(f'courses_page_{page}_cat_{instance.category_id}')
