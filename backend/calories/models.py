from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

class FoodCalorie(models.Model):
    consumed_at = models.DateTimeField()
    name = models.CharField(max_length=100)
    calorie = models.PositiveIntegerField()
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    is_inactive = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now())

    @classmethod
    def get_no_entries(cls, start, end):
        return cls.objects.filter(created_at__gte = start, created_at__lte = end).count()

    @classmethod
    def get_avg_calorie_per_user(cls, start, end):
        all_entries = cls.objects.filter(created_at__gte = start, created_at__lt = end)
        distinct_users_count = all_entries.values_list('user', flat=True).distinct().count()
        if distinct_users_count == 0:
            return float('NaN')
        total = all_entries.aggregate(models.Sum('calorie'))['calorie__sum']
        return total/distinct_users_count

    def __str__(self):
        return self.name