from django.db import models
from django.contrib.auth import get_user_model


class FoodCalorie(models.Model):
    consumed_at = models.DateTimeField()
    name = models.CharField(max_length=100)
    calorie = models.PositiveIntegerField()
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    is_inactive = models.BooleanField(default=False)

    def __str__(self):
        return self.name