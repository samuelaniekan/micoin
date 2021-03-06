from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import RefferalProfile,Account


@receiver(post_save, sender=Account)
def create_profile(sender, instance, created, **kwargs):
    if created:
        RefferalProfile.objects.create(user=instance)


@receiver(post_save, sender=Account)
def save_profile(sender, instance, **kwargs):
    instance.refferalprofile.save()