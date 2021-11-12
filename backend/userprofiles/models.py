from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    calorie_limit = models.PositiveIntegerField(default=2100)

    def __str__(self) -> str:
        return self.user.username

@receiver(post_save, sender=get_user_model())
def user_saved(sender, instance, **kwargs):
    try :
        user_profile = UserProfile.objects.get(user = instance)
    except Exception:
        user_profile = UserProfile.objects.create(user=instance)
        user_profile.save()
        
